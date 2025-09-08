# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collisions(player):
                sys.exit("Game Over!")
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collisions(shot):
                    asteroid.kill()
                    shot.kill()
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    print('''
          Starting Asteroids!
          Screen width: {SCREEN_WIDTH}
          Screen height: {SCREEN_HEIGHT}
          '''.format(SCREEN_WIDTH = SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_HEIGHT)
          )


if __name__ == "__main__":
    main()
