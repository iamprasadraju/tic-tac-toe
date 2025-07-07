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

    def draw_board(self):
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


    def play(self, win_moves):
        self.draw_board()
        pygame.display.flip()
        

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
                elif event.type == pygame.MOUSEBUTTONDOWN and self.move_count < 9:  
                    mouseX, mouseY = pygame.mouse.get_pos()
                    clicked_row = mouseY // self.CELL_SIZE
                    clicked_col = mouseX // self.CELL_SIZE
                    move  = (clicked_row + 1, clicked_col + 1)

                    if move not in self.visited_cells:
                        if self.move_count % 2 == 0:
                            self.draw_cross(clicked_row, clicked_col)
                            self.playerA_moves.append(move)
                        else:
                            self.draw_circle(clicked_row, clicked_col)
                            self.playerB_moves.append(move)
                            
                        self.visited_cells.append(move)
                        self.move_count += 1
                        pygame.display.flip()

                        # Check for win after this move
                        A = set(self.playerA_moves)
                        B = set(self.playerB_moves)

                        for line in win_moves:
                            if set(line).issubset(A):
                                print("Player A wins! - X")
                                pygame.display.set_caption("Player A wins! - X")
                                return self.playerA_moves, self.playerB_moves
                            elif set(line).issubset(B):
                                print("Player B wins! - O")
                                pygame.display.set_caption("Player B wins! - O")
                                return self.playerA_moves, self.playerB_moves

                    else:
                        print("Try Again !")

            if self.move_count >= 9:
                running = False

        return self.playerA_moves, self.playerB_moves
        
