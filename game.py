import random

import pygame
from board import Board

all_pos = [(row, col) for row in range(3) for col in range(3)]
WIN_POSITIONS = [
    # rows
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    # columns
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    # diagonals
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]


running = True


init_board = [[None, None, None], [None, None, None], [None, None, None]]


def HvsH(event):
    symbol = random.choice(["X", "O"])

    game.apply_move(event, symbol)


if __name__ == "__main__":
    game = Board()

    while game.running:
        game.draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                HvsH(event)
        pygame.display.flip()
    pygame.quit()
