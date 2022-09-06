import pygame
import random

pygame.init()

# Screen Variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAME_RATE = 30

COLOR_RED = (255,0,0)
COLOR_BLUE = (0,0,255)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0,255,0)

IS_GAME_OVER = False

# Common Constats: Player and Enemy
RECT_SIDE = 50
RECT_SIZE = (RECT_SIDE, RECT_SIDE)
STEP_SIZE_LEVEL_1 = 5
STEP_SIZE_LEVEL_2 = 10
STEP_SIZE_LEVEL_3 = 15
STEP_SIZE_LEVEL_4 = 20
STEP_SIZE_LEVEL_MAX = 25
PLAYER_STEP_SIZE = RECT_SIDE // 2

# Player Rectangle:
RECT_INIT_X = RECT_INIT_Y = 400

# Enemy Rectangle
ENMY_DROP_RATE = STEP_SIZE_LEVEL_1
ENMY_COUNT = 10

# Player Rectangle
player_ship = [RECT_INIT_X, RECT_INIT_Y]

# Enemy Rectangle
enemies = list()

# Clock
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dodge of Doom')

# Details for the score
score_font = pygame.font.SysFont('googlesans', 20)
score = 0

def generate_enemies(enemy_army: list, total_enemies: int):
    debris_probability = random.random()
    if (debris_probability > 0.1):
        return

    if len(enemy_army) < total_enemies:
        enemy_X = random.randint(0, SCREEN_WIDTH - RECT_SIDE)
        enemy_Y = 0
        enemy_army.append([enemy_X, enemy_Y])

def update_all_enemies(enemy_army, dodged_so_far, drop_rate):
    for indx, enemy_ship in enumerate(enemy_army):
        if enemy_ship[1] >= SCREEN_HEIGHT:
            enemy_army.pop(indx)
            dodged_so_far += 1
        else:
            enemy_ship[1] += drop_rate

    return (dodged_so_far)

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

def move_player_ship(player_ship):
    x_delta = y_delta = 0

    if game_event.type == pygame.KEYDOWN:
        print("KEY PRESSED")
        if game_event.key == pygame.K_LEFT:
            print('KEY: Left')
            x_delta -= PLAYER_STEP_SIZE

        elif game_event.key == pygame.K_RIGHT:
            print("KEY: Right")
            x_delta += PLAYER_STEP_SIZE 

        elif game_event.key == pygame.K_DOWN: 
            print("KEY: Right")
            y_delta += PLAYER_STEP_SIZE 
        
        elif game_event.key == pygame.K_UP:
            print("KEY: Right")
            y_delta -= PLAYER_STEP_SIZE 

        # Compute the new rect co-ordinates
        new_X = player_ship[0] + x_delta
        new_Y = player_ship[1] + y_delta
        if new_X >= 0 and new_X <= SCREEN_WIDTH - RECT_SIDE:
            player_ship[0] = new_X
        if new_Y >= 0 and new_Y <= SCREEN_HEIGHT - RECT_SIDE:
            player_ship[1] = new_Y

    # end if

def get_step_size(score):
    if score < 10:
        return STEP_SIZE_LEVEL_1
    elif score < 25:
        return STEP_SIZE_LEVEL_2
    elif score < 50:
        return STEP_SIZE_LEVEL_3
    elif score < 75:
        return STEP_SIZE_LEVEL_4
    else:
        return STEP_SIZE_LEVEL_MAX

def get_level(score):
    if score < 10:
        return '1'
    elif score < 25:
        return '2'
    elif score < 50:
        return '3'
    elif score < 75:
        return '4'
    else:
        return '5 (Max)'


# Main gaming loop
while not IS_GAME_OVER:

    # Generate multiple enemies
    generate_enemies(enemies, ENMY_COUNT)

    # 1. Determine the player's move
    for game_event in pygame.event.get():
        # 1.1 Process Quit events
        if game_event == pygame.QUIT:
            quit()
        
        # 1.2 Process any other arrow keys
        move_player_ship(player_ship)
 
    # 2. Set the canvas
    screen.fill((0,0,0))

    # Print debugs
    print('Player:', player_ship)

    # 3. Draw the player's ship
    PLAYER_RECTANGLE = pygame.Rect(player_ship, RECT_SIZE)
    pygame.draw.rect(screen, COLOR_RED, PLAYER_RECTANGLE)

    # 4. Draw the enemies ships
    for enemy_ship in enemies:
        ENMY_RECTANGLE = pygame.Rect(enemy_ship, RECT_SIZE)
        pygame.draw.rect(screen, COLOR_BLUE, ENMY_RECTANGLE)
    
    # 5. Check for any collisions
    if is_detected_collision_with_enemies(player_ship, enemies):
        print("GAME OVER!")
        IS_GAME_OVER = True

    # 6. Re-Compute Enemy ship positions
    score = update_all_enemies(enemies, score, get_step_size(score))
    score_text = "Level: " + get_level(score) + " Score : " + str(score)
    score_label = score_font.render(score_text, True, COLOR_GREEN, COLOR_BLUE)
    screen.blit(score_label, (0,0))

    # 7. Update the levels
    ENMY_DROP_RATE = get_step_size(score)

    # 8. Paint the frame
    clock.tick(FRAME_RATE)
    pygame.display.update()

#end while

# Print final parameters
print('Level: ' + get_level(score) + ', Score: ' + str(score))
quit()