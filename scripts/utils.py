import os
import random
import sys
from typing import Tuple, List

import pygame

from scripts.button import Button
from scripts.canvas import Canvas


# TODO: Maybe reorganize this so that class-specific functions [like generate_random_button()]
#  are instead defined in the relevant class module
# TODO: Adjust generate_random_button() to ensure that generated buttons do not overlap other buttons.
#  while self.image_rect.colliderect(other_button.image_rect):
#   position = [random.randint(0, canvas.dimensions[0] - 100), random.randint(0, canvas.dimensions[1] - 100)]


def generate_random_button(canvas: Canvas, text: str, image_path: str, scale: float, existing_buttons: List[Button], moving_button: bool = True,
                           generate_sparks_toggle: bool = False, has_collision: bool = False) -> Button:
    position = create_position(canvas)
    while any(button.image_rect.colliderect(pygame.Rect(position, (100, 100))) for button in existing_buttons):
        position = create_position(canvas)
    if moving_button:
        velocity = [random.randint(-5, 5), random.randint(-5, 5)]  # This can return [0, 0]
        while velocity == [0, 0]:  # Ensure button has non-zero velocity
            velocity = [random.randint(-5, 5), random.randint(-5, 5)]
    else:
        velocity = [0, 0]
    return Button(canvas=canvas, text=text, image_path=image_path, position=position, scale=scale, velocity=velocity,
                  generate_sparks_toggle=generate_sparks_toggle, has_collision=has_collision)


def quit_game() -> None:
    pygame.quit()
    sys.exit(0)


def create_position(canvas: Canvas):
    # Offset the bounds of the randint() call so that button doesn't get stuck at the bottom/left side
    return [random.randint(0, canvas.dimensions[0] - 100), random.randint(0, canvas.dimensions[1] - 100)]


def get_random_image(image_directory: str, return_text: bool = False) -> Tuple[str, str]:
    files = os.listdir(image_directory)
    image_files = [file for file in files if file.lower().endswith('.png')]
    random_image = random.choice(image_files)
    filename_without_extension = os.path.splitext(random_image)[0] if return_text else None
    return random_image, filename_without_extension

