#!/usr/bin/env python
import pygame


pygame.init()

WIDTH = 500
HEIGHT = 500
    
# Window size (Tic-tac-toe Board) 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Line color is White (255, 255, 255) RBG
LINE_COLOR = (255, 255, 255) # pygame.color("white")
LINE_WIDTH = 2
CELL_SIZE = WIDTH // 3

def Board():
    screen.fill((0, 0, 0))
    

    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, HEIGHT), LINE_WIDTH)


    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0,2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE), LINE_WIDTH)

   

def draw_circle(row, col):
    center_x = col * CELL_SIZE + CELL_SIZE // 2
    center_y = row * CELL_SIZE + CELL_SIZE // 2
    radius = CELL_SIZE // 3
    pygame.draw.circle(screen, LINE_COLOR, (center_x, center_y), radius, LINE_WIDTH)

def draw_cross(row, col):
    padding = 33
    start_x = col * CELL_SIZE + padding
    start_y = row * CELL_SIZE + padding
    end_x = (col + 1) * CELL_SIZE - padding
    end_y = (row + 1) * CELL_SIZE - padding

    # Line from top-left to bottom-right
    pygame.draw.line(screen, LINE_COLOR, (start_x, start_y), (end_x, end_y), LINE_WIDTH)

    # Line from top-right to bottom-left
    pygame.draw.line(screen, LINE_COLOR, (end_x, start_y), (start_x, end_y), LINE_WIDTH)

def main():
    Board()
    pygame.display.flip()
    count  = 1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = mouseY // CELL_SIZE
                clicked_col = mouseX // CELL_SIZE
                if count % 2 == 0 and count < 9:
                    draw_circle(clicked_row, clicked_col)
                    count += 1
                    pygame.display.flip()
                else:
                    draw_cross(clicked_row, clicked_col)
                    pygame.display.flip()
                    count += 1
    
    pygame.quit()


main()