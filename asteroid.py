import pygame
import random
from circleshape import CircleShape
from logger import log_event
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if (self.radius > ASTEROID_MIN_RADIUS):
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(angle)
            velocity2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first = Asteroid(self.position.x, self.position.y, new_radius)
            first.velocity = velocity1 * 1.2
            print(f"Split asteroid:\n\tfirst fragment angle {angle}")
            second = Asteroid(self.position.x, self.position.y, new_radius)
            second.velocity = velocity2 * 1.2
            print(f"\tsecond fragment angle {-angle}")



    