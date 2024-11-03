import sys
from typing import Tuple

import pygame


class Canvas:
    def __init__(self, dimensions: Tuple[int, int] = (1280, 720), title: str = "Game"):
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


class Button:
    def __init__(self, text: str, image_path: str, position: Tuple[int, int], canvas: Canvas, scale: float = 1.0):
        self.text = text
        self.position = position
        self.canvas = canvas
        self.font = pygame.font.Font(None, 36)
        self.scale = scale
        self.image = pygame.image.load(image_path).convert_alpha() if image_path else None
        self.image_rect = None
        self.image_mask = None
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
            return self.image_mask.get_at(relative_pos) if 0 <= relative_pos[0] < self.image_rect.width and 0 <= \
                                                           relative_pos[1] < self.image_rect.height else False
        else:
            return self.image_rect.collidepoint(mouse_pos)


def main():
    pygame.init()
    canvas = Canvas()
    IMAGE_DIRECTORY = '../resources/images/'

    # Create buttons with scaling
    angry_birds_button = Button(text=None, image_path=f'{IMAGE_DIRECTORY}angry_birds.png', position=(200, 200),
                                canvas=canvas, scale=1)
    play_button = Button(text='Play', image_path=f'{IMAGE_DIRECTORY}play_button.png', position=(200, 200),
                         canvas=canvas, scale=0.5)
    quit_button = Button(text='Quit', image_path=f'{IMAGE_DIRECTORY}quit_button.png', position=(900, 200),
                         canvas=canvas, scale=0.25)

    running = True
    while running:
        canvas.fill((255, 255, 255))

        # Keep in mind order of drawing is important, only top-most button in overlap will get clicked
        angry_birds_button.draw()
        play_button.draw()
        quit_button.draw()
        canvas.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button.is_clicked(mouse_pos):
                    print("Play button clicked!")
                elif angry_birds_button.is_clicked(mouse_pos):
                    print("Angry birds button clicked!")
                elif quit_button.is_clicked(mouse_pos):
                    print("Quit button clicked!")
                    running = False

    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()
