import math
import random
from typing import List

import pygame


class Spark:
    def __init__(self, position: List[int], angle: float = None, speed: float = 1.0):
        self.position = position
        self.angle = angle if angle is not None else random.random() * 2 * math.pi  # Angle in radians, default random
        self.speed = speed

    def update(self):
        self.position[0] += self.speed * math.cos(self.angle)
        self.position[1] += self.speed * math.sin(self.angle)
        self.speed = max(0.0, self.speed - 0.1)
        return not self.speed

    def render(self, surface, offset=(0, 0)):
        render_points = [
            (self.position[0] + math.cos(self.angle) * self.speed * 3 - offset[0],
             self.position[1] + math.sin(self.angle) * self.speed * 3 - offset[1]),
            (self.position[0] + math.cos(self.angle + math.pi * 0.5) * self.speed - offset[0],
             self.position[1] + math.sin(self.angle + math.pi * 0.5) * self.speed - offset[1]),
            (self.position[0] + math.cos(self.angle + math.pi) * self.speed * 3 - offset[0],
             self.position[1] + math.sin(self.angle + math.pi) * self.speed * 3 - offset[1]),
            (self.position[0] + math.cos(self.angle - math.pi * 0.5) * self.speed - offset[0],
             self.position[1] + math.sin(self.angle - math.pi * 0.5) * self.speed - offset[1]),
        ]
        pygame.draw.polygon(surface, (255, 255, 255), render_points)
