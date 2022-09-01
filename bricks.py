from cmath import rect
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
ENMY_DROP_RATE = 25

# Player Rectangle
rect_pos = (RECT_INIT_X, RECT_INIT_Y)
x = rect_pos[0]
y = rect_pos[1]

# Enemy Rectangle
enmy_rect_pos = (ENMY_RECT_INIT_X, ENMY_RECT_INIT_Y)
enmy_x = enmy_rect_pos[0]
enmy_y = enmy_rect_pos[1]

# Clock
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
            rect_pos = (x, y)

    # Compute Enemy rectangle 
    enmy_y += ENMY_DROP_RATE
    enmy_rect_pos = (enmy_x, enmy_y)
    screen.fill((0,0,0))

    # Print debugs
    print('Player:', rect_pos)
    print('Enemy:', enmy_rect_pos)

    # Draw the rectangles
    PLAYER_RECTANGLE = pygame.Rect(rect_pos, RECT_SIZE)
    pygame.draw.rect(screen, COLOR_RED, PLAYER_RECTANGLE)

    ENMY_RECTANGLE = pygame.Rect(enmy_rect_pos, RECT_SIZE)
    pygame.draw.rect(screen, COLOR_BLUE, ENMY_RECTANGLE)

    clock.tick(FRAME_RATE)
    # Refresh the screen
    pygame.display.update()