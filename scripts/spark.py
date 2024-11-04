import math
import random
from typing import List, Tuple

import pygame


class Spark:
    def __init__(self, position: List[int], angle: float = None, speed: float = 1.0, size: float = 30.0,
                 color: Tuple[int, int, int] = (0, 0, 0)):
        self.position = position
        self.angle = angle if angle is not None else random.random() * 2 * math.pi  # Angle in radians, default random
        self.speed = speed # Frame duration of spark is effectively speed / deceleration from update()
        self.size = size
        self.color = color

    def update(self, deceleration: float = 0.1) -> bool:
        self.position[0] += self.speed * math.cos(self.angle)
        self.position[1] += self.speed * math.sin(self.angle)
        self.speed = max(0.0, self.speed - deceleration)
        return self.speed == 0.0

    def render(self, surface: pygame.Surface, offset: Tuple[int, int] = (0, 0)) -> None:
        render_points = [ # Ugly
            (self.position[0] + math.cos(self.angle) * self.speed * self.size - offset[0],
             self.position[1] + math.sin(self.angle) * self.speed * self.size - offset[1]),
            (self.position[0] + math.cos(self.angle + math.pi * 0.5) * self.speed * (self.size / 3) - offset[0],
             self.position[1] + math.sin(self.angle + math.pi * 0.5) * self.speed * (self.size / 3) - offset[1]),
            (self.position[0] + math.cos(self.angle + math.pi) * self.speed * self.size - offset[0],
             self.position[1] + math.sin(self.angle + math.pi) * self.speed * self.size - offset[1]),
            (self.position[0] + math.cos(self.angle - math.pi * 0.5) * self.speed * (self.size / 3) - offset[0],
             self.position[1] + math.sin(self.angle - math.pi * 0.5) * self.speed * (self.size / 3) - offset[1]),
        ]
        pygame.draw.polygon(surface, self.color, render_points)
