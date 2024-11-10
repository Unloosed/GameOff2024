
# TODO: Fix this absolute garbage.
#  The buttons get stuck on walls and just slide along them instead of reversing direction.
#   This has to do with Button's has_button_collision attribute, which somehow messes it up when False

class MovementPattern:
    def __init__(self, movement_pattern_name: str, button, speed: int = 2) -> None:
        self.speed = speed
        button.velocity = [self.speed, self.speed]
        self.movement_pattern_name = movement_pattern_name
        self.movement_patterns = {
            'up_and_down': self.up_and_down,
            'side_to_side': self.side_to_side,
            'diagonal': self.diagonal,
        }

    def perform_movement_pattern(self, button) -> None:
        if self.movement_pattern_name in self.movement_patterns:
            self.movement_patterns[self.movement_pattern_name](button)
        else:
            print(f"Unknown movement pattern: {self.movement_pattern_name}")

    def is_button_y_position_out_of_bounds(self, button) -> bool:
        return button.position[1] <= 0 or button.position[1] + button.image_rect.height >= button.canvas.dimensions[1]

    def is_button_x_position_out_of_bounds(self, button) -> bool:
        return button.position[0] <= 0 or button.position[0] + button.image_rect.width >= button.canvas.dimensions[0]

    def up_and_down(self, button) -> None:
        button.position[1] += button.velocity[1]
        if self.is_button_y_position_out_of_bounds(button):
            button.velocity[1] = -button.velocity[1]
            # Ensure the button is fully inside the boundary after bounce
            button.position[1] = max(0, min(button.position[1], button.canvas.dimensions[1] - button.image_rect.height))

    def side_to_side(self, button) -> None:
        button.position[0] += button.velocity[0]
        if self.is_button_x_position_out_of_bounds(button):
            button.velocity[0] = -button.velocity[0]
            # Ensure the button is fully inside the boundary after bounce
            button.position[0] = max(0, min(button.position[0], button.canvas.dimensions[0] - button.image_rect.width))

    def diagonal(self, button) -> None:
        button.position[0] += button.velocity[0]
        button.position[1] += button.velocity[1]
        button.check_collision()

        # if self.is_button_x_position_out_of_bounds(button):
        #     button.velocity[0] = -button.velocity[0]
        #     # Ensure the button is fully inside the boundary after bounce
        #     button.position[0] = max(0, min(button.position[0], button.canvas.dimensions[0] - button.image_rect.width))
        # if self.is_button_y_position_out_of_bounds(button):
        #     button.velocity[1] = -button.velocity[1]
        #     # Ensure the button is fully inside the boundary after bounce
        #     button.position[1] = max(0, min(button.position[1], button.canvas.dimensions[1] - button.image_rect.height))
