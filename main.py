import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0 # delta time
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # pygame groups
    grp_updatable = pygame.sprite.Group()
    grp_drawable = pygame.sprite.Group()
    grp_asteroids = pygame.sprite.Group()
    grp_shots = pygame.sprite.Group()

    # set containers
    Player.containers = (grp_drawable, grp_updatable)
    Asteroid.containers = (grp_asteroids, grp_updatable, grp_drawable)
    AsteroidField.containers = (grp_updatable)
    Shot.containers = (grp_shots, grp_updatable, grp_drawable)

    # create game objects
    player_ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, grp_shots)
    asteroid_field = AsteroidField()


    game_loop = True
    while game_loop:
        # check if the user has closed the window and exit the game loop if they do.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))

        grp_updatable.update(dt)
        player_ship.shoot_cooldown -= dt

        for drawable in grp_drawable:
            drawable.draw(screen)

        for asteroid in grp_asteroids:
            if asteroid.collision_chk(player_ship):
                print("Game Over!")
                raise SystemExit
            for bullet in grp_shots:
                if asteroid.collision_chk(bullet):
                    asteroid.kill()
                    bullet.kill()

        pygame.display.flip()
        
        dt = clock.tick(60)/1000  # pause for 60 ms and return the delta time in sec since last call

if __name__ == "__main__":
    main()