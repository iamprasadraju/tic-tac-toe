import pygame

pygame.init()

WIDTH = 500
ROWS = 3

# Window size
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Tic Tac Toe")

GRAY = (128, 128, 128)

running = True

X_IMAGE = pygame.transform.scale(pygame.image.load("assets/x.png"), (80, 80))
O_IMAGE = pygame.transform.scale(pygame.image.load("assets/o.png"), (80, 80))


class Board:
    def __init__(self):
        self.running = True

    # Apply the move on Screen
    def apply_move(self, symbol):
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = event.pos  # Get mouse click co-ordinates

            if symbol == "O":
                screen.blit(O_IMAGE, (m_x, m_y))
            elif symbol == "X":
                screen.blit(X_IMAGE, (m_x, m_y))

    def render_board(self):
        pass

    def grid(self):
        gap = WIDTH // ROWS

        # Starting points
        x = 0
        y = 0

        for i in range(ROWS):
            x = i * gap

            pygame.draw.line(screen, GRAY, (x, 0), (x, WIDTH), 3)
            pygame.draw.line(screen, GRAY, (0, x), (WIDTH, x), 3)

        pygame.display.flip()


if __name__ == "__main__":
    Game = Board()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        Game.grid()
        Game.move("X")

        pygame.display.flip()
    pygame.quit()
