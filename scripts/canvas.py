from typing import Tuple

import pygame


class Canvas:
    def __init__(self, dimensions: Tuple[int, int] = (1280, 720), title: str = "I Am Spy"):
        self.dimensions = dimensions
        self.screen = pygame.display.set_mode(dimensions)
        pygame.display.set_caption(title)
        self.print_dimensions()

    def print_dimensions(self):
        print(f'Canvas Dimensions: {self.dimensions}')

    def fill(self, color: Tuple[int, int, int] = (255, 255, 255)):
        self.screen.fill(color)

    def update(self):
        pygame.display.flip()
