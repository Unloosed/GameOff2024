import random
import sys

import pygame

from scripts.button import Button
from scripts.canvas import Canvas


# TODO: Maybe reorganize this so that class-specific functions [like generate_random_button()]
#  are instead defined in the relevant class module


def generate_random_button(canvas: Canvas, image_path: str, scale: float, moving_button: bool = True,
                           generate_sparks_toggle: bool = False) -> Button:
    # Offset the bounds of the randint() call so that button doesn't get stuck at the bottom/left side
    position = [random.randint(0, canvas.dimensions[0] - 100), random.randint(0, canvas.dimensions[1] - 100)]
    if moving_button:
        velocity = [random.randint(-5, 5), random.randint(-5, 5)]  # This can return [0, 0]
        while velocity == [0, 0]:  # Ensure button has non-zero velocity
            velocity = [random.randint(-5, 5), random.randint(-5, 5)]
    else:
        velocity = [0, 0]
    return Button(canvas=canvas, image_path=image_path, position=position, scale=scale, velocity=velocity,
                  generate_sparks_toggle=generate_sparks_toggle)


def quit_game() -> None:
    pygame.quit()
    sys.exit(0)
