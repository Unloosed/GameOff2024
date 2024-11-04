from typing import List, Optional

import pygame


# TODO: Deal with buttons with no image. They load just fine, but they are hard to click since you have to click the
#  actual text instead of an invisible rectangle that encloses the text
# TODO: Implement priority functionality such that if two buttons are being clicked on a single mouse click,
#  only register the higher-priority button click.
# TODO: Implement priority functionality such that higher-priority buttons are rendered on top of lower-priority buttons


class Button:
    def __init__(self, canvas, text: Optional[str] = None, image_path: Optional[str] = None,
                 position: Optional[List[int]] = None, scale: float = 1.0,
                 priority: int = 1, velocity: Optional[List[int]] = None):
        self.canvas = canvas
        self.text = text
        self.position = position if position else [100, 100]  # Top left corner of button
        self.font = pygame.font.Font(None, 36)
        self.scale = scale
        self.image = pygame.image.load(image_path).convert_alpha() if image_path else None
        self.image_rect = None
        self.image_mask = None
        self.priority = priority
        self.velocity = velocity if velocity else [0, 0]
        self.setup()

    def setup(self):
        if self.image:
            width, height = self.image.get_size()
            scaled_size = (int(width * self.scale), int(height * self.scale))
            self.image = pygame.transform.scale(self.image, scaled_size)
            self.image_rect = self.image.get_rect(topleft=self.position)
            self.image_mask = pygame.mask.from_surface(self.image)
        else:
            self.image_rect = pygame.Rect(self.position, (int(100 * self.scale), int(50 * self.scale)))

    def draw(self):
        if self.image:
            self.canvas.screen.blit(self.image, self.image_rect)
        if self.text:
            text_surface = self.font.render(self.text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=self.image_rect.center)
            self.canvas.screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        if self.image_mask:
            relative_pos = (mouse_pos[0] - self.image_rect.x, mouse_pos[1] - self.image_rect.y)
            return self.image_mask.get_at(relative_pos) if 0 <= relative_pos[0] < self.image_rect.width and \
                                                           0 <= relative_pos[1] < self.image_rect.height else False
        else:
            return self.image_rect.collidepoint(mouse_pos)

    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.image_rect.topleft = self.position

        # Check for collisions with the edges of the screen and reverse direction if needed
        if self.image_rect.left <= 0 or self.image_rect.right >= self.canvas.dimensions[0]:
            self.velocity[0] = -self.velocity[0]
        if self.image_rect.top <= 0 or self.image_rect.bottom >= self.canvas.dimensions[1]:
            self.velocity[1] = -self.velocity[1]
