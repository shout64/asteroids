import pygame
import random as r
from constants import ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle              = r.uniform(20, 50)
            new_asteroid_one_velocity = self.velocity.rotate(random_angle)
            new_asteroid_two_velocity = self.velocity.rotate(-random_angle)
            new_radius                = self.radius - ASTEROID_MIN_RADIUS
            speed_multiplier          = 1.2

            new_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid_one.velocity = new_asteroid_one_velocity * speed_multiplier
            new_asteroid_two.velocity = new_asteroid_two_velocity * speed_multiplier
            