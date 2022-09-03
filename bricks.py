from cmath import rect
from re import L, T
import pygame
import sys
import random

pygame.init()

# Screen Variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAME_RATE = 30

COLOR_RED = (255,0,0)
COLOR_BLUE = (0,0,255)

IS_GAME_OVER = False

# Common Constats: Player and Enemy
RECT_SIDE = 50
RECT_SIZE = (RECT_SIDE, RECT_SIDE)
STEP_SIZE = RECT_SIDE//2

# Player Rectangle:
RECT_INIT_X = RECT_INIT_Y = 400

# Enemy Rectangle
ENMY_RECT_INIT_X = random.randint(0, SCREEN_WIDTH - RECT_SIDE)
ENMY_RECT_INIT_Y = 0
ENMY_DROP_RATE = 10
ENMY_COUNT = 5

# Player Rectangle
player_ship = [RECT_INIT_X, RECT_INIT_Y]
x = player_ship[0]
y = player_ship[1]

# Enemy Rectangle
enemy_ship = [ENMY_RECT_INIT_X, ENMY_RECT_INIT_Y]
enmy_x = enemy_ship[0]
enmy_y = enemy_ship[1]
enemies = list()

# Clock
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def generate_enemies(enemy_army: list, total_enemies: int):
    debris_probability = random.random()
    if (debris_probability > 0.1):
        return

    if len(enemy_army) < total_enemies:
        enemy_X = random.randint(0, SCREEN_HEIGHT - RECT_SIDE)
        enemy_Y = ENMY_RECT_INIT_Y
        enemy_army.append([enemy_X, enemy_Y])

def update_all_enemies(enemy_army):
    for indx, enemy_ship in enumerate(enemy_army):
        if enemy_ship[1] >= SCREEN_HEIGHT:
            enemy_army.pop(indx)
            print("Removed Enemy Ship[", indx, "]")
        else:
            enemy_ship[1] += ENMY_DROP_RATE

def is_detected_collision_with_enemies(player, enemy_army):
    for enemy in enemy_army:
        if is_detected_collision_with_enemy(player, enemy, RECT_SIDE):
            return True
        
    return False

def is_detected_collision_with_enemy(player_block, enemy_block, BLOCK_SIZE):
    player_X = player_block[0]
    enemy_X = enemy_block[0]

    player_Y = player_block[1]
    enemy_Y = enemy_block[1]

    if (enemy_X > player_X - BLOCK_SIZE) and (enemy_X < player_X + BLOCK_SIZE):
        if (enemy_Y > player_Y - BLOCK_SIZE) and (enemy_Y < player_Y + BLOCK_SIZE):
            print("Collison detected. Enemy:", enemy_block, "Player:", player_block)
            return True
    # endif

    return False

# Generate multiple enemies
generate_enemies(enemies, ENMY_COUNT)
x_delta = y_delta = 0

while not IS_GAME_OVER:
    for game_event in pygame.event.get():

        # Process key events
        if game_event == pygame.QUIT:
            sys.exit()

        if game_event.type == pygame.KEYDOWN:
            print("KEY PRESSED")
            if game_event.key == pygame.K_LEFT:
                print('KEY: Left')
                x_delta = y_delta = 0
                x_delta -= STEP_SIZE

            elif game_event.key == pygame.K_RIGHT:
                print("KEY: Right")
                x_delta = y_delta = 0
                x_delta += STEP_SIZE 

            elif game_event.key == pygame.K_DOWN: 
                print("KEY: Right")
                x_delta = y_delta = 0
                y_delta += STEP_SIZE 
            
            elif game_event.key == pygame.K_UP:
                print("KEY: Right")
                x_delta = y_delta = 0
                y_delta -= STEP_SIZE 

            # Compute the new rect co-ordinates
            x += x_delta
            y += y_delta
            player_ship = [x, y]

    screen.fill((0,0,0))

    # Print debugs
    print('Player:', player_ship)
    print('Enemy :', enemy_ship)

    # Draw the rectangles
    PLAYER_RECTANGLE = pygame.Rect(player_ship, RECT_SIZE)
    pygame.draw.rect(screen, COLOR_RED, PLAYER_RECTANGLE)

    for enemy_ship in enemies:
        ENMY_RECTANGLE = pygame.Rect(enemy_ship, RECT_SIZE)
        pygame.draw.rect(screen, COLOR_BLUE, ENMY_RECTANGLE)
    
    if is_detected_collision_with_enemies(player_ship, enemies):
        print("GAME OVER!")
        IS_GAME_OVER = True

    # Refresh the screen
    clock.tick(FRAME_RATE)
    pygame.display.update()

    # Re-Compute Enemy rectangle
    update_all_enemies(enemies)
    generate_enemies(enemies, ENMY_COUNT)

#end while
sys.exit()