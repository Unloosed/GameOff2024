import random

from scripts.button import Button
from scripts.canvas import Canvas


def generate_random_button(canvas: Canvas, image_path: str, scale: float) -> Button:
    position = [random.randint(0, canvas.dimensions[0] - 100), random.randint(0, canvas.dimensions[1] - 50)]
    velocity = [random.randint(-5, 5), random.randint(-5, 5)]  # This can return [0, 0]
    while velocity == [0, 0]:  # Ensure buttons have non-zero velocity
        velocity = [random.randint(-5, 5), random.randint(-5, 5)]
    return Button(canvas=canvas, image_path=image_path, position=position, scale=scale, velocity=velocity)
