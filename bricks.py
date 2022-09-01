from cmath import rect
import pygame
import sys

pygame.init()

# Screen Variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

IS_GAME_OVER = False

# Rectangle Parameters
COLOR_RED = (255,0,0)
RECT_INIT_X = RECT_INIT_Y = 400
RECT_SIDE = 50
RECT_SIZE = (RECT_SIDE, RECT_SIDE)
STEP_SIZE = RECT_SIDE//2

rect_pos = (RECT_INIT_X, RECT_INIT_Y)
x = rect_pos[0]
y = rect_pos[1]

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

    # Refresh the screen
    pygame.display.update()