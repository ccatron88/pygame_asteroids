# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black", rect=None)
        pygame.display.flip()

    print('''
          Starting Asteroids!
          Screen width: {SCREEN_WIDTH}
          Screen height: {SCREEN_HEIGHT}
          '''.format(SCREEN_WIDTH = SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_HEIGHT)
          )


if __name__ == "__main__":
    main()
