#!/usr/bin/env python
import pygame
import sys
import random
from board import Board



def copy_board(original):
    new_board = Board(draw_enabled = False)
    new_board.visited_cells = original.visited_cells.copy()
    new_board.playerA_moves = original.playerA_moves.copy()
    new_board.playerB_moves = original.playerB_moves.copy()
    new_board.move_count = original.move_count
    return new_board

def MiniMax(game_state, is_maximizing, computer_sym): # without Depth Because it's a small gaame
    result = game_state.check_win()

    if result is not None:
        if result == 1:  # X wins
            return 1 if computer_sym == 'X' else -1
        elif result == -1:  # O wins
            return 1 if computer_sym == 'O' else -1
        else:  # Draw
            return 0

    if is_maximizing:
        best_value = float('-inf')
        for move in game_state.get_available_moves():
            new_board = copy_board(game_state)
            new_board.apply_move(move, computer_sym)
            value = MiniMax(new_board, False, computer_sym)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        opponent_sym = 'O' if computer_sym == 'X' else 'X'
        for move in game_state.get_available_moves():
            new_board = copy_board(game_state)
            new_board.apply_move(move, opponent_sym)
            value = MiniMax(new_board, True, computer_sym)
            best_value = min(best_value, value)
        return best_value

def find_best_move(board, computer_sym):
    best_move = None
    best_value = float('-inf')
    available_moves = board.get_available_moves()

    for move in available_moves:
        new_board = copy_board(board)
        new_board.apply_move(move, computer_sym)
        move_value = MiniMax(new_board, False, computer_sym)
        if move_value > best_value:
            best_value = move_value
            best_move = move

    return best_move


def CvsH():
    board = Board(draw_enabled=True)
    human_sym = random.choice(["X", "O"])
    computer_sym = "O" if human_sym == "X" else "X"

    board.board_ui()
    pygame.display.flip()

    # Computer first move if computer is X
    if computer_sym == "X" and board.move_count == 0:
        first_move = random.choice(board.get_available_moves())
        board.apply_move(first_move, computer_sym)
        pygame.display.set_caption("Your Turn")
        pygame.display.flip()
    else:
        pygame.display.set_caption("Your Turn")

    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif not game_over and event.type == pygame.MOUSEBUTTONDOWN and board.move_count < 9:
                mouseX, mouseY = pygame.mouse.get_pos()
                row = mouseY // board.CELL_SIZE
                col = mouseX // board.CELL_SIZE
                move = (row + 1, col + 1)

                if board.apply_move(move, human_sym):
                    result = board.check_win()
                    if result is not None:
                        game_over = True
                        board.gameOver_ui(result, human_sym)
                        break

                    pygame.display.set_caption("Computer's Turn")
                    pygame.display.flip()

                    if board.move_count < 9:
                        pygame.time.delay(500)
                        move = find_best_move(board, computer_sym)
                        if move:
                            board.apply_move(move, computer_sym)
                            result = board.check_win()
                            if result is not None:
                                game_over = True
                                board.gameOver_ui(result, human_sym)
                                break
                            pygame.display.set_caption("Your Turn")
                            pygame.display.flip()
                else:
                    print("Invalid move. Try again!")

            elif game_over and event.type == pygame.MOUSEBUTTONDOWN:
                if board.restart_button and board.restart_button.collidepoint(event.pos):
                    board.reset()
                    game_over = False
                    if computer_sym == "X":
                        first_move = random.choice(board.get_available_moves())
                        board.apply_move(first_move, computer_sym)
                    pygame.display.set_caption("Your Turn" if human_sym == "X" else "Computer's Turn")
                    pygame.display.flip()


def HvsH():
    board = Board(draw_enabled=True)
    board.board_ui()
    pygame.display.flip()

    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            elif not game_over and event.type == pygame.MOUSEBUTTONDOWN and board.move_count < 9:
                mouseX, mouseY = pygame.mouse.get_pos()
                row = mouseY // board.CELL_SIZE
                col = mouseX // board.CELL_SIZE
                move = (row + 1, col + 1)

                current_player = "X" if board.move_count % 2 == 0 else "O"
                if board.apply_move(move, current_player):
                    result = board.check_win()
                    if result is not None:
                        game_over = True
                        board.gameOver_ui(result)
                else:
                    print("Invalid move. Try again!")

            elif game_over and event.type == pygame.MOUSEBUTTONDOWN:
                if board.restart_button and board.restart_button.collidepoint(event.pos):
                    board.reset()
                    game_over = False


            

if __name__ == "__main__":
    board = Board()
    board.Home_ui()
    choice = board.handle_home_events()
    if choice == "CvsH":
        CvsH()
    elif choice == "HvsH":
        HvsH()