import pygame
from constants import *
import player

def main():
    print("Starting Asteroids!")

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player_ship = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    game_loop = True
    while game_loop:
        # check if the user has closed the window and exit the game loop if they do.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))

        player_ship.update(dt)

        player_ship.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60)/1000  # pause for 60 ms and return the delta time in sec since last call

if __name__ == "__main__":
    main()