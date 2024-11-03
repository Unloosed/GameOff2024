from typing import Tuple

import pygame

# from scripts.settings import *

class Canvas():
    def __init__(self, dimensions: Tuple[int, int] = (800, 600)):
        self.dimensions = dimensions
        self.screen = pygame.display.set_mode(dimensions)

    def print_dimensions(self):
        print(f'Dimensions: {self.dimensions}')

# button(image_path="/image.png", text='')
class Button():
    def __init__(self, text: str, image_path: str, position: Tuple[int, int], canvas: Canvas, dimensions: Tuple[int, int] = (800, 600)):
        if text is not None:
            self.text = text
        if image_path is not None:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image_rect = self.image.get_rect(topleft=position)  # Position the image
            # Create a mask for the image to match its non-rectangular shape
            self.image_mask = pygame.mask.from_surface(self.image)
            canvas.screen.blit(self.image, self.image_rect)

        self.dimensions = dimensions


my_canvas = Canvas()
my_canvas.print_dimensions()


# Load the PNG image with transparency
IMAGE_DIRECTORY = '../resources/images/'

my_button = Button(text = None, image_path=(IMAGE_DIRECTORY + 'angry_birds.png'), canvas=my_canvas, dimensions=(100,100), position=(200,200))

running = True
image = pygame.image.load(IMAGE_DIRECTORY + 'angry_birds.png').convert_alpha()  # Use convert_alpha for transparency
while running:
    image_rect = image.get_rect(topleft=(100, 100))  # Position the image

    # Create a mask for the image to match its non-rectangular shape
    my_canvas.screen.fill((255, 255, 255))

    # Draw the image
    my_canvas.screen.blit(image, image_rect)

    # Update display
    pygame.display.flip()
