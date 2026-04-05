from typing import Tuple

import pygame


# board ui and actions
class Board:
    def __init__(
        self, screen, window_size: Tuple[int, int] = (500, 500)
    ):  # window size default (500px * 500px)
        self.width, self.height = window_size

        self.screen = screen
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

    def draw_grid(self, grid_size: tuple):
        rows, cols = grid_size

        # draw horizontal lines
        for i in range(1, rows):
            # Calculate y-coordinate for each horizontal divider
            y_pos = (i * self.height) // rows
            pygame.draw.line(self.screen, self.WHITE, (0, y_pos), (self.width, y_pos))

        # 2. Draw Vertical Lines
        for j in range(1, cols):
            # Calculate x-coordinate for each vertical divider
            x_pos = (j * self.width) // cols
            pygame.draw.line(self.screen, self.WHITE, (x_pos, 0), (x_pos, self.height))
