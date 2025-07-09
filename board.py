#!/usr/bin/env python
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

class Board():
    def __init__(self):
        self.LINE_COLOR = (255, 255, 255)
        self.LINE_WIDTH = 2
        self.CELL_SIZE = WIDTH // 3

        self.visited_cells = []
        self.playerA_moves = []  # X
        self.playerB_moves = []  # O
        self.move_count = 0

        # Create winning positions
        board_positions = [[(i, j) for j in range(1, 4)] for i in range(1, 4)]
        vertical_positions = [[board_positions[row][col] for row in range(3)] for col in range(3)]
        horizontal_positions = board_positions
        diagonal_positions = [
            [board_positions[i][i] for i in range(3)],
            [board_positions[i][2 - i] for i in range(3)]
        ]

        self.win_moves = vertical_positions + horizontal_positions + diagonal_positions

    def board_ui(self):
        screen.fill((0, 0, 0))  # Black background

        # Draw grid
        pygame.draw.line(screen, self.LINE_COLOR, (self.CELL_SIZE, 0), (self.CELL_SIZE, HEIGHT), self.LINE_WIDTH)
        pygame.draw.line(screen, self.LINE_COLOR, (2 * self.CELL_SIZE, 0), (2 * self.CELL_SIZE, HEIGHT), self.LINE_WIDTH)
        
        pygame.draw.line(screen, self.LINE_COLOR, (0, self.CELL_SIZE), (WIDTH, self.CELL_SIZE), self.LINE_WIDTH)
        pygame.draw.line(screen, self.LINE_COLOR, (0, 2 * self.CELL_SIZE), (WIDTH, 2 * self.CELL_SIZE), self.LINE_WIDTH)

    def draw_circle(self, row, col):
        center_x = col * self.CELL_SIZE + self.CELL_SIZE // 2
        center_y = row * self.CELL_SIZE + self.CELL_SIZE // 2
        radius = self.CELL_SIZE // 3
        pygame.draw.circle(screen, self.LINE_COLOR, (center_x, center_y), radius, self.LINE_WIDTH)

    def draw_cross(self, row, col):
        padding = 33
        start_x = col * self.CELL_SIZE + padding
        start_y = row * self.CELL_SIZE + padding
        end_x = (col + 1) * self.CELL_SIZE - padding
        end_y = (row + 1) * self.CELL_SIZE - padding

        pygame.draw.line(screen, self.LINE_COLOR, (start_x, start_y), (end_x, end_y), self.LINE_WIDTH)
        pygame.draw.line(screen, self.LINE_COLOR, (end_x, start_y), (start_x, end_y), self.LINE_WIDTH)


    def apply_move(self, move, player_symbol):
        row, col = move[0] - 1, move[1] - 1
        if move in self.visited_cells:
            return False

        self.visited_cells.append(move)

        if player_symbol == "X":
            self.draw_cross(row, col)
            self.playerA_moves.append(move)
            pygame.display.set_caption("O Turn !")
        else:
            self.draw_circle(row, col)
            self.playerB_moves.append(move)
            pygame.display.set_caption("X Turn !")

        self.move_count += 1
        pygame.display.flip()
        return True