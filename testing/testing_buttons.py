import pygame

from scripts.button import Button, handle_click, draw_buttons_by_priority
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

    buttons = [angry_birds_button, play_button, quit_button, text_button]

    # Generate additional random buttons
    for _ in range(num_random_buttons):
        buttons.append(generate_random_button(canvas, f'{image_directory}play_button.png', 0.1))

    running = True
    while running:
        canvas.fill((255, 255, 255))

        for button in buttons:
            button.move()
            #button.draw()

        draw_buttons_by_priority(buttons)
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
