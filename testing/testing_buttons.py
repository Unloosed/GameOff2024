import pygame

from scripts.button import Button, handle_click, draw_buttons, move_buttons, sort_buttons_by_priority
from scripts.canvas import Canvas
from scripts.utils import generate_random_button, quit_game, get_random_image, generate_patterned_buttons


def main(image_directory: str = '../resources/images/', num_random_buttons: int = 20):
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
    birds_directory = f'{image_directory}birds/'

    # Different methods for generating buttons. One includes a pattern (broken), the other one doesn't (sorta broken)
    # generate_random_buttons_no_pattern(birds_directory, buttons, canvas, num_random_buttons)
    # buttons = generate_random_buttons_with_pattern(birds_directory, buttons, canvas, num_random_buttons)

    buttons = sort_buttons_by_priority(buttons)

    # Start game loop
    running = True
    while running:
        canvas.fill()

        move_buttons(buttons)
        draw_buttons(buttons)
        canvas.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                running = handle_click(buttons, mouse_pos)

        clock.tick(30)  # 30 frames/second
    quit_game()  # End game loop


def generate_random_buttons_with_pattern(birds_directory, buttons, canvas, num_random_buttons):
    images = []
    texts = []
    for _ in range(num_random_buttons):
        image, text = get_random_image(birds_directory)
        images.append(f'{birds_directory}{image}')
        texts.append(text)
    buttons += generate_patterned_buttons(canvas, texts, images, 0.1, existing_buttons=buttons,
                                          generate_sparks_toggle=True, has_button_collision=True,
                                          movement_pattern_name='diagonal')
    return buttons


def generate_random_buttons_no_pattern(birds_directory, buttons, canvas, num_random_buttons):
    for _ in range(num_random_buttons):
        image, text = get_random_image(birds_directory)
        buttons.append(generate_random_button(canvas, text, f'{birds_directory}{image}', 0.1,
                                              existing_buttons=buttons, generate_sparks_toggle=True,
                                              has_button_collision=True))


if __name__ == "__main__":
    main()
