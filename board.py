import math

import pygame

pygame.init()

WIDTH = 500
ROWS = 3
CELL_SIZE = WIDTH // ROWS


# Window size
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Tic Tac Toe")
running = True


GRAY = (128, 128, 128)
WHITE = (255, 255, 255)

screen.fill(WHITE)


X_IMAGE = pygame.transform.scale(pygame.image.load("assets/x.png"), (100, 100))
O_IMAGE = pygame.transform.scale(pygame.image.load("assets/o.png"), (100, 100))


class Board:
    def __init__(self):
        self.running = True

    # Apply the move on Screen
    def apply_move(self, event, symbol):
        m_x, m_y = event.pos  # Get mouse click co-ordinates

        row = m_y // CELL_SIZE
        col = m_x // CELL_SIZE

        # center the image in the cell
        pos_x = col * CELL_SIZE + (CELL_SIZE - 100) // 2
        pos_y = row * CELL_SIZE + (CELL_SIZE - 100) // 2

        if symbol == "O":
            screen.blit(O_IMAGE, (pos_x, pos_y))
        elif symbol == "X":
            screen.blit(X_IMAGE, (pos_x, pos_y))

    def render_board(self):
        pass

    def draw_grid(self):
        gap = WIDTH // ROWS

        # Starting points
        x = 0
        y = 0

        for i in range(ROWS):
            x = i * gap

            pygame.draw.line(screen, GRAY, (x, 0), (x, WIDTH), 3)
            pygame.draw.line(screen, GRAY, (0, x), (WIDTH, x), 3)

        pygame.display.flip()


"""

if __name__ == "__main__":
    Game = Board()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        Game.grid()
        Game.apply_move()

        pygame.display.flip()
    pygame.quit()



"""
