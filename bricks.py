import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

IS_GAME_OVER = False

# Rectangle Parameters
COLOR_RED = (255,0,0)
RECT_POS = (400, 400)
RECT_SIDE = 50
RECT_SIZE = (RECT_SIDE, RECT_SIDE)

PLAYER_RECTANGLE = pygame.Rect(RECT_POS, RECT_SIZE)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while not IS_GAME_OVER:
    for game_event in pygame.event.get():

        # Debugging only
        print(game_event)

        # Process key events
        if game_event == pygame.QUIT:
            sys.exit()

        if game_event.type == pygame.KEYDOWN:
            print("KEY DOWN")
            if game_event.key == pygame.K_LEFT:
                print("KEY_LEFT-ANSH")
            elif game_event.key == pygame.K_RIGHT:
                print("KEY_RIGHT")

    # Draw a rectangle
    pygame.draw.rect(screen, COLOR_RED, PLAYER_RECTANGLE)

    # Refresh the screen
    pygame.display.update()