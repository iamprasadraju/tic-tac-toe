import random

import pygame

from board import Board

# Initialize the pygame display
pygame.init()


# pygame window size (in pixels)
width = 600
height = 600

# pygame.display.init()
screen = pygame.display.set_mode(size=(width, height))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()  # Limits FPS

ttt_board = Board(screen)  # window size default (500px * 500px)


def run():
    running = True
    while running:
        screen.fill((0, 0, 0))
        ttt_board.event_screen("home")

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            """
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    row, col = ttt_board.get_mouse_gridnum(event.pos)

                    player = random.choice(["X", "O"])
                    ttt_board.player_move(player, (row, col))
            """

        # ttt_board.draw_grid()  # Draw the White grid
        ttt_board.event_screen(event="home")

        pygame.display.update()

        # Update the display
        pygame.display.flip()

        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    run()
