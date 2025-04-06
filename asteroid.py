import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    """Asteroid sprite class for Asteroids game"""
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color=(255,255,255), # RGB tuple for white
            center=(self.position.x, self.position.y),
            radius= self.radius,
            width=2
        )

    def update(self, dt):
        self.position += self.velocity * dt 