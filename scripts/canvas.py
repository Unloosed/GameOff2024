from typing import Tuple

import pygame


# TODO: Add functionality to scale Canvas from settings.py


class Canvas:
    def __init__(self, dimensions: Tuple[int, int] = (1280, 720), title: str = "I Am Spy",
                 color: Tuple[int, int, int] = (255, 255, 255)):
        self.dimensions = dimensions
        self.title = title
        self.color = color
        self.screen = pygame.display.set_mode(dimensions)
        pygame.display.set_caption(self.title)
        self.print_dimensions()

    def print_dimensions(self) -> None:
        print(f'Canvas Dimensions: {self.dimensions}')

    def fill(self) -> None:
        self.screen.fill(self.color)

    def update(self) -> None:
        pygame.display.flip()
