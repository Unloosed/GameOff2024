import os
import random
import sys
from typing import Tuple, List, Optional

import pygame

from scripts.button import Button
from scripts.canvas import Canvas


# TODO: patterned_buttons() is incomplete!
# TODO: Maybe reorganize this so that class-specific functions [like generate_random_button()]
#  are instead defined in the relevant class module


def generate_random_button(canvas: Canvas, text: str, image_path: str, scale: float, existing_buttons: List[Button],
                           moving_button: bool = True,
                           generate_sparks_toggle: bool = False, has_button_collision: bool = False,
                           movement_pattern_name: Optional[str] = None) -> Button:
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
                  generate_sparks_toggle=generate_sparks_toggle, has_button_collision=has_button_collision,
                  movement_pattern_name=movement_pattern_name)


def generate_patterned_buttons(canvas: Canvas, texts: List[str], image_paths: List[str], scale: float, existing_buttons: List[Button],
                               moving_button: bool = True,
                               generate_sparks_toggle: bool = False, has_button_collision: bool = False,
                               movement_pattern_name: Optional[str] = None) -> List[Button]:
    buttons = []
    for text, image_path in zip(texts, image_paths):
        buttons.append(generate_random_button(canvas, text, image_path, scale, existing_buttons, moving_button,
                                              generate_sparks_toggle, has_button_collision, movement_pattern_name))
    buttons_with_patterned_coordinates = patterned_buttons(buttons)
    return buttons_with_patterned_coordinates


def patterned_buttons(buttons: List[Button]) -> List[Button]:
    # Organizes list of buttons into a pattern
    return buttons


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
