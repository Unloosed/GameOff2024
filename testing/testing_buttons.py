import sys

import pygame

from scripts.button import Button
from scripts.canvas import Canvas
from scripts.utils import generate_random_button


def main():
    pygame.init()
    canvas = Canvas()
    clock = pygame.time.Clock()
    IMAGE_DIRECTORY = '../resources/images/'

    # Create stationary buttons
    angry_birds_button = Button(canvas=canvas, text='Angry Birds', image_path=f'{IMAGE_DIRECTORY}angry_birds.png',
                                position=[300, 300], scale=0.2)
    play_button = Button(canvas=canvas, text='Play', image_path=f'{IMAGE_DIRECTORY}play_button.png',
                         position=[200, 200], scale=0.2)
    quit_button = Button(canvas=canvas, text='Quit', image_path=f'{IMAGE_DIRECTORY}quit_button.png',
                         position=[900, 200], scale=0.1)

    buttons = [angry_birds_button, play_button, quit_button]

    # Generate additional random buttons
    for _ in range(10):
        buttons.append(generate_random_button(canvas, f'{IMAGE_DIRECTORY}play_button.png', 0.1))

    running = True
    while running:
        canvas.fill((255, 255, 255))

        for button in buttons:
            button.move()
            button.draw()

        canvas.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.is_clicked(mouse_pos):
                        print(f"{button.text} button clicked!")
                        if button.text == 'Quit':
                            running = False

        clock.tick(30)

    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()
