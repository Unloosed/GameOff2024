from typing import List, Optional, Tuple

import pygame

from scripts.spark import Spark


# TODO: Add better toggles (likely from settings.py) that control toggles globally (like button sparks)
# TODO: Dynamic render priority, not sure if it's worth it. Seems to affect performance a lot b/c of sorting
# TODO: Create new Button (or Button attribute?) that links to RPG (object of interest button)


class Button:
    def __init__(self, canvas, text: Optional[str] = None, image_path: Optional[str] = None,
                 position: Optional[List[int]] = None, scale: float = 1.0,
                 priority: int = 1, velocity: Optional[List[int]] = None,
                 generate_sparks_toggle: bool = False):
        self.canvas = canvas
        self.text = text
        self.position = position if position else [100, 100] # Top left corner of button
        self.font = pygame.font.Font(None, 36)
        self.scale = scale
        self.image = pygame.image.load(image_path).convert_alpha() if image_path else None
        self.image_rect = None
        self.image_mask = None
        self.priority = priority # Higher priority renders on top & gets clicked first
        self.velocity = velocity if velocity else [0, 0]
        self.sparks = []
        self.generate_sparks_toggle = generate_sparks_toggle
        self.setup()

    def setup(self) -> None:
        if self.image: # Scale image and set up the rect and mask
            width, height = self.image.get_size()
            scaled_size = (int(width * self.scale), int(height * self.scale))
            self.image = pygame.transform.scale(self.image, scaled_size)
            self.image_rect = self.image.get_rect(topleft=self.position)
            self.image_mask = pygame.mask.from_surface(self.image)
        else: # If text only, make a rectangle so that you don't have to click exactly where the text is rendered
            text_surface = self.font.render(self.text, True, (0, 0, 0))
            width, height = text_surface.get_size()
            self.image_rect = pygame.Rect(self.position, (width, height))

    def draw(self) -> None:
        if self.image: # Simple blit
            self.canvas.screen.blit(self.image, self.image_rect)
        if self.text: # Maybe text_surface and text_rect should be attributes?
            text_surface = self.font.render(self.text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=self.image_rect.center)
            self.canvas.screen.blit(text_surface, text_rect)
        for spark in self.sparks:
            spark.render(self.canvas.screen)

    def is_clicked(self, mouse_pos: Tuple[int, int]) -> bool:
        if self.image:
            relative_pos = (mouse_pos[0] - self.image_rect.x, mouse_pos[1] - self.image_rect.y)
            return self.image_mask.get_at(relative_pos) if 0 <= relative_pos[0] < self.image_rect.width and \
                                                           0 <= relative_pos[1] < self.image_rect.height else False
        else:
            return self.image_rect.collidepoint(mouse_pos)

    def move(self) -> None:
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.image_rect.topleft = self.position # Update image_rect using new position

        collision_side = self.check_collision()
        if collision_side and self.generate_sparks_toggle:
            self.generate_sparks(collision_side)
        if self.generate_sparks_toggle:
            self.update_sparks()

    def check_collision(self):
        # Flip relevant velocity, otherwise return None (no collision)
        if self.image_rect.left <= 0:
            self.velocity[0] = -self.velocity[0]
            return 'left'
        elif self.image_rect.right >= self.canvas.dimensions[0]:
            self.velocity[0] = -self.velocity[0]
            return 'right'
        elif self.image_rect.top <= 0:
            self.velocity[1] = -self.velocity[1]
            return 'top'
        elif self.image_rect.bottom >= self.canvas.dimensions[1]:
            self.velocity[1] = -self.velocity[1]
            return 'bottom'
        return None

    def generate_sparks(self, side: str, num_sparks: int = 3, spark_offset: Tuple[int, int] = (40, 20)) -> None:
        spark_position = list(self.position)
        # Need to adjust spark_position because otherwise it generates at the top left corner of the rect
        if side == 'left':
            spark_position[0] = self.image_rect.left + spark_offset[0]
            spark_position[1] = self.image_rect.top + spark_offset[1]
        elif side == 'right':
            spark_position[0] = self.image_rect.right - spark_offset[0]
            spark_position[1] = self.image_rect.bottom - spark_offset[1]
        elif side == 'top':
            spark_position[1] = self.image_rect.top + spark_offset[1]
            spark_position[0] = self.image_rect.left + spark_offset[0]
        elif side == 'bottom':
            spark_position[1] = self.image_rect.bottom - spark_offset[1]
            spark_position[0] = self.image_rect.right - spark_offset[0]

        for _ in range(num_sparks):
            spark = Spark(position=spark_position, size=5.0)
            self.sparks.append(spark)

    def update_sparks(self) -> None:
        # Update all sparks, keep the sparks that don't reach speed 0
        self.sparks = [spark for spark in self.sparks if not spark.update()]


def handle_click(buttons: List[Button], mouse_pos: Tuple[int, int]) -> bool:
    sorted_buttons = sorted(buttons, key=lambda b: b.priority, reverse=True)
    for button in sorted_buttons:
        if button.is_clicked(mouse_pos):
            print(f"{button.text} button clicked!")
            if button.text == 'Quit':
                return False  # Stop the game loop if 'Quit' is clicked
    return True


def sort_buttons_by_priority(buttons: List[Button]) -> List[Button]:
    return sorted(buttons, key=lambda b: b.priority)


def draw_buttons(buttons: List[Button]) -> None:
    for button in buttons:
        button.draw()


def move_buttons(buttons: List[Button]) -> None:
    for button in buttons:
        button.move()
