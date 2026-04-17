#!/usr/bin/env python3

import random

import pygame

from board import Board

# Initialize the pygame display
pygame.init()

# pygame window size (in pixels)
width = 600
height = 600
num_cells = (3, 3)


# pygame.display.init()
screen = pygame.display.set_mode(size=(width, height))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()  # Limits FPS

ttt_board = Board(screen)  # window size default (500px * 500px)


def check_winner(player_moves):
    for comb in ttt_board.all_win_moves:
        if all(pos in player_moves for pos in comb):
            return True
    return False


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
                    pygame.display.set_caption(f"{ttt_board.current_player} Turn")

                elif ttt_board.hvsai_btn.is_clicked(event):
                    ttt_board.board_state = "playing"
                    pygame.display.set_caption(f"{ttt_board.current_player} Turn")
            elif ttt_board.board_state == "game_over":
                if ttt_board.play_again.is_clicked(event):
                    ttt_board.reset_game()

            elif ttt_board.board_state == "playing":
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    row, col = ttt_board.get_mouse_gridnum(event.pos)
                    move = (row, col)
                    max_moves = num_cells[0] * num_cells[1]

                    # make move for current player
                    if len(ttt_board.moves) < max_moves:
                        if move not in ttt_board.moves:
                            ttt_board.player_move((row, col))

                            if ttt_board.current_player == "X":
                                if check_winner(ttt_board.X_moves):
                                    pygame.display.set_caption("X Wins!")
                                    ttt_board.board_state = "game_over"
                                    continue
                                ttt_board.current_player = "O"
                            else:
                                if check_winner(ttt_board.O_moves):
                                    pygame.display.set_caption("O Wins!")
                                    ttt_board.board_state = "game_over"
                                    continue
                                ttt_board.current_player = "X"
                                pygame.display.flip()

                            pygame.display.set_caption(
                                f"{ttt_board.current_player} Turn"
                            )
                        else:
                            pygame.display.set_caption("Invalid move")

        if ttt_board.board_state == "start":
            ttt_board.screen.fill(ttt_board.BLACK)
            ttt_board.event_screen("home")

        elif ttt_board.board_state == "game_over":
            ttt_board.draw_win_screen()

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
