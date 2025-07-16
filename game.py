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

def end_game(result, human_sym):
    if result == 0:
        print("Draw!")
    elif (result == 1 and human_sym == "X") or (result == -1 and human_sym == "O"):
        print("Human Wins!")
    else:
        print("Computer Wins!")
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

def CvsH():
    board = Board(draw_enabled=True)
    human_sym = random.choice(["X", "O"])
    computer_sym = "O" if human_sym == "X" else "X"

    board.board_ui()
    pygame.display.flip()

    if computer_sym == "X":
        pygame.time.delay(500)
        move = find_best_move(board, computer_sym)
        if move:
            board.apply_move(move, computer_sym)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            is_human_turn = ((board.move_count % 2 == 0 and human_sym == "X") or
                             (board.move_count % 2 == 1 and human_sym == "O"))

            if is_human_turn and event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                row = mouseY // board.CELL_SIZE
                col = mouseX // board.CELL_SIZE
                move = (row + 1, col + 1)

                if board.apply_move(move, human_sym):
                    result = board.check_win()
                    if result is not None:
                        end_game(result, human_sym)

                    pygame.display.set_caption("Computer's Turn")
                    pygame.display.flip()

                    if board.move_count < 9:
                        pygame.time.delay(500)
                        move = find_best_move(board, computer_sym)
                        if move:
                            board.apply_move(move, computer_sym)
                            result = board.check_win()
                            if result is not None:
                                end_game(result, human_sym)
                            pygame.display.set_caption("Your Turn")
                            pygame.display.flip()
                else:
                    print("Invalid move. Try again!")

def HvsH():
    board = Board(draw_enabled=True)
    board.board_ui()
    pygame.display.flip()
    while True:
        move = board.mouse_click()
        current_player = "X" if board.move_count % 2 == 0 else "O"
        if board.apply_move(move, current_player):
            result = board.check_win()
            if result is not None:
                if result == 0:
                    print("Draw!")
                elif result == 1:
                    print("X wins!")
                else:
                    print("O wins!")
                pygame.time.wait(2000)
                pygame.quit()
                sys.exit()
        else:
            print("Invalid move. Try again!")

if __name__ == "__main__":
    pygame.init()
    CvsH()   # Human vs Computer
    # HvsH()  # Uncomment to test Human vs Human
