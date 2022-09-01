from cmath import rect
from curses import COLOR_BLACK
import pygame
import sys

pygame.init()

# Screen Variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

IS_GAME_OVER = False

# Common Constats: Player and Enemy
RECT_SIDE = 50
RECT_SIZE = (RECT_SIDE, RECT_SIDE)
STEP_SIZE = RECT_SIDE//2

# Player Rectangle:
COLOR_RED = (255,0,0)
RECT_INIT_X = RECT_INIT_Y = 400

# Enemy Rectangle
COLOR_BLUE = (0,0,255)
ENMY_RECT_INIT_X = 100
ENMY_RECT_INIT_Y = 0

# Player Rectangle
rect_pos = (RECT_INIT_X, RECT_INIT_Y)
x = rect_pos[0]
y = rect_pos[1]

# E
enem_rect_pos = (ENMY_RECT_INIT_X, ENMY_RECT_INIT_Y)

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
            print(rect_pos)

    screen.fill((0,0,0))

    # Draw a rectangle
    PLAYER_RECTANGLE = pygame.Rect(rect_pos, RECT_SIZE)
    pygame.draw.rect(screen, COLOR_RED, PLAYER_RECTANGLE)

    ENMY_RECTANGLE = pygame.Rect(enem_rect_pos, RECT_SIZE)
    pygame.draw.rect(screen, COLOR_BLUE, ENMY_RECTANGLE)

    # Refresh the screen
    pygame.display.update()