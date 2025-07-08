#!/usr/bin/env python
import pygame
import sys


pygame.init()

WIDTH = 500
HEIGHT = 500
    
# Window size (Tic-tac-toe Board) 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

class Board():
    def __init__(self):
        self.LINE_COLOR = (255, 255, 255)
        self.LINE_WIDTH = 2
        self.CELL_SIZE = WIDTH // 3

        self.visited_cells = []
        self.move_count  = 0
        self.playerA_moves = [] # X moves
        self.playerB_moves = [] # O moves

        board_positions = [[(i, j) for j in range(1, 4)] for i in range(1, 4)]
        horizontal_positions = board_positions.copy()
        vertical_positions = []
        # vertical_positions  = [[board_positions[row][col] for row in range(3)] for col in range(3)]

        for col in range(3):
            vertical = []
            for row in range(3):
                vertical.append(board_positions[row][col])
            vertical_positions.append(vertical)
        diagonal_positions = [
            [board_positions[i][i] for i in range(3)],
            [board_positions[i][2 - i] for i in range(3)]
        ]

        self.win_moves = vertical_positions + horizontal_positions + diagonal_positions

    def board_ui(self):
        screen.fill((0, 0, 0)) # Black
        
        # Draw 2 horizontal lines 
        pygame.draw.line(screen, self.LINE_COLOR, (self.CELL_SIZE, 0), (self.CELL_SIZE, HEIGHT), self.LINE_WIDTH)
        pygame.draw.line(screen, self.LINE_COLOR, (2 * self.CELL_SIZE, 0), (2 * self.CELL_SIZE, HEIGHT), self.LINE_WIDTH)

        # Draw 2 vertical lines
        pygame.draw.line(screen, self.LINE_COLOR, (0, self.CELL_SIZE), (WIDTH, self.CELL_SIZE), self.LINE_WIDTH)
        pygame.draw.line(screen, self.LINE_COLOR, (0,2 * self.CELL_SIZE), (WIDTH, 2 * self.CELL_SIZE), self.LINE_WIDTH)

   

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

        # Line from top-left to bottom-right
        pygame.draw.line(screen, self.LINE_COLOR, (start_x, start_y), (end_x, end_y), self.LINE_WIDTH)

        # Line from top-right to bottom-left
        pygame.draw.line(screen, self.LINE_COLOR, (end_x, start_y), (start_x, end_y), self.LINE_WIDTH)


    def check_win(self):
        # Check for win after this move
        A = set(self.playerA_moves)
        B = set(self.playerB_moves)

        for line in self.win_moves:
            if set(line).issubset(A):
                pygame.display.set_caption("Player A wins! - X")
                # if a player wins sys.exit
                return "X"
            elif set(line).issubset(B):
                pygame.display.set_caption("Player B wins! - O")
                return "O"

    def move(self):
        # Get Mouse click Co-ordinate  
        mouseX, mouseY = pygame.mouse.get_pos()
        clicked_row = mouseY // self.CELL_SIZE
        clicked_col = mouseX // self.CELL_SIZE
        move  = (clicked_row + 1, clicked_col + 1)

        if move not in self.visited_cells:
            if self.move_count % 2 == 0:
                self.draw_cross(clicked_row, clicked_col)
                self.playerA_moves.append(move)
                pygame.display.set_caption("O Turn !")
            else:
                self.draw_circle(clicked_row, clicked_col)
                self.playerB_moves.append(move)
                pygame.display.set_caption("X Turn !")
                
            self.visited_cells.append(move)
            self.move_count += 1
            # Update the Screen
            pygame.display.flip()

        else:
            print("Try Again !")

    
    def play(self):
        self.board_ui()
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
                elif event.type == pygame.MOUSEBUTTONDOWN and self.move_count < 9:
                    self.move()

            self.check_win()

        if self.move_count >= 9:
                    running = False

"""board = Board()
board.play()"""