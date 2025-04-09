import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20, 50)  # in degrees
            vect_1 = self.velocity.rotate(split_angle)
            vect_2 = self.velocity.rotate(-split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            A_1 = Asteroid(self.position.x, self.position.y, new_radius)
            A_2 = Asteroid(self.position.x, self.position.y, new_radius)
            A_1.velocity = vect_1 * 1.2
            A_2.velocity = vect_2 * 1.2
