#!/usr/bin/env python
import pygame


pygame.init()

WIDTH = 500
HEIGHT = 500
    
# Window size (Tic-tac-toe Board) 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

class Borad():
    def __init__(self):
        self.LINE_COLOR = (255, 255, 255)
        self.LINE_WIDTH = 2
        self.CELL_SIZE = WIDTH // 3

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


    def play(self):
        self.draw_board()
        pygame.display.flip()
        count  = 1
        visited = []

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    
                    mouseX, mouseY = pygame.mouse.get_pos()
                    clicked_row = mouseY // self.CELL_SIZE
                    clicked_col = mouseX // self.CELL_SIZE
                    if (clicked_row, clicked_col) not in visited:
                        if count % 2 == 0 and count < 9:
                            self.draw_circle(clicked_row, clicked_col)
                            visited.append((clicked_row, clicked_col))
                            count += 1
                            pygame.display.flip()
                        else:
                            self.draw_cross(clicked_row, clicked_col)
                            visited.append((clicked_row, clicked_col))
                            pygame.display.flip()
                            count += 1
        pygame.quit()

game = Borad()
game.play()