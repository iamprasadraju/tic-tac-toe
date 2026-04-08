from typing import Tuple

import pygame

from effects import ConfettiEffect


class Button:
    def __init__(self, text, x, y, width, height, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        # Loading font once in init is better for performance
        self.font = pygame.font.Font("assets/PixeloidSans.ttf", 18)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        is_hovering = self.rect.collidepoint(mouse_pos)

        if is_hovering:
            # FILLED rectangle on hover
            pygame.draw.rect(screen, self.hover_color, self.rect, border_radius=15)
            text_color = (255, 255, 255)  # White text when filled
        else:
            # BORDER only when not hovering (width=3)
            pygame.draw.rect(screen, self.color, self.rect, width=3, border_radius=15)
            text_color = self.color  # Text matches border color

        # Render text and center it
        text_surf = self.font.render(self.text, True, text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False


# board ui and actions
class Board:
    def __init__(
        self,
        screen,
        window_size: Tuple[int, int] = (600, 600),
        num_cells: Tuple[int, int] = (3, 3),
    ):  # window size default (600px * 600px) and nums_cells (3, 3)
        self.width, self.height = window_size

        # num of rows and cols
        self.rows, self.cols = num_cells

        # calculate cell size  (w and h)
        self.CELLSIZE_W = self.width // self.cols
        self.CELLSIZE_H = self.height // self.rows

        self.screen = screen
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREY = (128, 128, 128)
        self.GREYRED = (153, 3, 3)

        # Board state (playing, tie, win)
        self.board_state = "playing"

        self.confetti = ConfettiEffect(self.screen)

        self.hvsh_btn = Button(
            "Human vs Human", 200, 200, 200, 70, "green", "green"
        )  # x, y, width, height
        self.hvsai_btn = Button("Human vs AI", 200, 350, 200, 70, "green", "green")

        self.home_font = pygame.font.Font("assets/PixeloidSans-Bold.ttf", 35)

    def draw_grid(self):
        # draw horizontal lines
        for i in range(1, self.rows):
            # Calculate y-coordinate for each horizontal divider
            y_pos = i * self.CELLSIZE_H
            pygame.draw.line(self.screen, self.WHITE, (0, y_pos), (self.width, y_pos))

        # draw Vertical Lines
        for j in range(1, self.cols):
            # Calculate x-coordinate for each vertical divider
            x_pos = j * self.CELLSIZE_W
            pygame.draw.line(self.screen, self.WHITE, (x_pos, 0), (x_pos, self.height))

    def player_move(self, player: str, grid_num: Tuple[int, int]):
        row, col = grid_num

        # X player move
        if player == "X":
            pad = 40

            x = col * self.CELLSIZE_W
            y = row * self.CELLSIZE_H

            top_left = (x + pad, y + pad)
            top_right = (x + self.CELLSIZE_W - pad, y + pad)
            bottom_left = (x + pad, y + self.CELLSIZE_H - pad)
            bottom_right = (x + self.CELLSIZE_W - pad, y + self.CELLSIZE_H - pad)

            pygame.draw.line(
                self.screen, self.GREYRED, top_left, bottom_right, width=30
            )
            pygame.draw.line(
                self.screen, self.GREYRED, top_right, bottom_left, width=30
            )

        # O player move
        elif player == "O":
            center = (
                col * self.CELLSIZE_W + (self.CELLSIZE_W // 2),
                row * self.CELLSIZE_H + (self.CELLSIZE_H // 2),
            )

            radius = (
                (self.CELLSIZE_H + self.CELLSIZE_W) / 2
            ) * 0.4  # radius will be 40% of cell size
            pygame.draw.circle(self.screen, self.GREY, center, radius, width=20)

    # to get grid num (0, 0) from mouse click
    def get_mouse_gridnum(self, mouse_pos):
        x, y = mouse_pos  # mouse click co-ord

        row_num = y // self.CELLSIZE_H
        col_num = x // self.CELLSIZE_W

        print(row_num, col_num)

        return (row_num, col_num)

    # TODO:custom event handling for tie, win, start, home screens
    def event_screen(self, event=None):
        if event == 1:
            self.screen.fill(SELF.BLACK)  # dark background
            self.confetti.update()
            self.confetti.draw()

        elif event == "home":
            text_surf = self.home_font.render("Tic Tac Toe", True, self.WHITE)
            self.screen.blit(text_surf, (172, 60))

            self.hvsh_btn.draw(self.screen)
            self.hvsai_btn.draw(self.screen)
