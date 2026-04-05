import pygame

from board import Board

# Initialize the pygame display
pygame.init()


# pygame window size (in pixels)
width = 500
height = 500

# pygame.display.init()
screen = pygame.display.set_mode(size=(width, height))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()  # Limits FPS

ttt_board = Board(screen)  # window size default (500px * 500px)


def run():
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        ttt_board.draw_grid((3, 3))  # Draw the White grid
        # Update the display
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    run()
