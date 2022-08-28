import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

IS_GAME_OVER = False

# Rectangle Parameters
COLOR_RED = (255,0,0)
RECT_X = RECT_Y = 400
RECT_POS = (RECT_X, RECT_Y)
RECT_SIDE = 50
RECT_SIZE = (RECT_SIDE, RECT_SIDE)
STEP_SIZE = RECT_SIDE//2

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
                HORIZ_STEP = VERTICAL_STEP = 0
                HORIZ_STEP += STEP_SIZE

            elif game_event.key == pygame.K_RIGHT:
                print("KEY: Right")
                HORIZ_STEP = VERTICAL_STEP = 0
                HORIZ_STEP -= STEP_SIZE 

            # Compute the new rect co-ordinates
            RECT_Y += VERTICAL_STEP
            RECT_X -= HORIZ_STEP
            RECT_POS = (RECT_X , RECT_Y)
            print(RECT_POS)

    screen.fill((0,0,0))

    # Draw a rectangle
    PLAYER_RECTANGLE = pygame.Rect(RECT_POS, RECT_SIZE)
    pygame.draw.rect(screen, COLOR_RED, PLAYER_RECTANGLE)

    # Refresh the screen
    pygame.display.update()