import sys
import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
from constants import *
from logger import log_state, log_event
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    
    # set up screen and context
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # set up groups, players, and asteroids
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        # CHECK for quit (ctrl-c)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)
        # check for collisions
        for asteroid in asteroids:
            # check for last-minute bullets first
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                sys.exit()
        
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
