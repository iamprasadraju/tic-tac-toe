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
    ttt_board.board_state = "start"
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif ttt_board.board_state == "start":
                if ttt_board.hvsh_btn.is_clicked(event):
                    ttt_board.board_state = "playing"
                elif ttt_board.hvsai_btn.is_clicked(event):
                    ttt_board.board_state = "playing"

            elif ttt_board.board_state == "playing":
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    row, col = ttt_board.get_mouse_gridnum(event.pos)
                    player = random.choice(["X", "O"])
                    ttt_board.player_move(player, (row, col))

        if ttt_board.board_state == "start":
            ttt_board.screen.fill(ttt_board.BLACK)
            ttt_board.event_screen("home")

        elif ttt_board.board_state == "playing":
            if not ttt_board.grid_drawn:
                ttt_board.screen.fill(ttt_board.BLACK)
                ttt_board.draw_grid()
                ttt_board.grid_drawn = True

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    run()
