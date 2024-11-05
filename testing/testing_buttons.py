import random

import pygame

from scripts.button import Button, handle_click, draw_buttons, sort_buttons_by_priority
from scripts.canvas import Canvas
from scripts.utils import generate_random_button, quit_game


def main(image_directory: str = '../resources/images/', num_random_buttons: int = 10):
    pygame.init()
    canvas = Canvas()
    clock = pygame.time.Clock()

    # Create stationary buttons
    angry_birds_button = Button(canvas=canvas, text='Angry Birds', image_path=f'{image_directory}angry_birds.png',
                                position=[100, 100], scale=0.5, priority=3)
    play_button = Button(canvas=canvas, text='Play', image_path=f'{image_directory}play_button.png',
                         position=[200, 200], scale=0.2, priority=2)
    quit_button = Button(canvas=canvas, text='Quit', image_path=f'{image_directory}quit_button.png',
                         position=[900, 200], scale=0.1, priority=1)
    text_button = Button(canvas=canvas, text='Text only')
    bird1 = Button(canvas=canvas, text='Bird png', image_path=f'{image_directory}bird bomb.png',
                         position=[200, 200], scale=0.2, priority=2, velocity=[random.randrange(1,10),random.randrange(1,10)])
    bird2 = Button(canvas=canvas, text='Bird png', image_path=f'{image_directory}bird chuck.webp',
                   position=[200, 200], scale=0.2, priority=2, velocity=[random.randrange(1,10),random.randrange(1,10)])
    bird3 = Button(canvas=canvas, text='Bird png', image_path=f'{image_directory}bird eagle.png',
                   position=[200, 200], scale=0.2, priority=2, velocity=[random.randrange(1,10),random.randrange(1,10)])
    bird4 = Button(canvas=canvas, text='Bird png', image_path=f'{image_directory}bird ice.webp',
                   position=[200, 200], scale=0.2, priority=2, velocity=[random.randrange(1,10),random.randrange(1,10)])
    bird5 = Button(canvas=canvas, text='Bird png', image_path=f'{image_directory}bird matilda.webp',
                   position=[200, 200], scale=0.2, priority=2, velocity=[random.randrange(1,10),random.randrange(1,10)])
    bird6 = Button(canvas=canvas, text='Bird png', image_path=f'{image_directory}bird red.webp',
                   position=[200, 200], scale=0.2, priority=2, velocity=[random.randrange(1,10),random.randrange(1,10)])
    bird7 = Button(canvas=canvas, text='Bird png', image_path=f'{image_directory}bird terence.webp',
                   position=[200, 200], scale=0.2, priority=2, velocity=[random.randrange(1,10),random.randrange(1,10)])

    buttons = [angry_birds_button, play_button, quit_button, text_button, bird1, bird2, bird3, bird4, bird5, bird6, bird7]

    # Generate additional random buttons
    for _ in range(num_random_buttons):
        buttons.append(
            generate_random_button(canvas, f'{image_directory}play_button.png', 0.1, generate_sparks_toggle=True))
    buttons = sort_buttons_by_priority(buttons)

    running = True
    while running:
        canvas.fill()

        for button in buttons:
            button.move()
            #button.draw()

        draw_buttons(buttons)
        canvas.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                running = handle_click(buttons, mouse_pos)

        clock.tick(30)

    quit_game()


if __name__ == "__main__":
    main()
