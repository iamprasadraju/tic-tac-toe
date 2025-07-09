from board import Board
import random
import pygame
import sys

board = Board()


def CvsH():
    seq = ["X", "O"]
    human_sym = random.choice(seq)
    computer_sym = "O" if human_sym == "X" else "X"

    board.board_ui()
    pygame.display.flip()
    running = True

    while running:
        # Human move
        is_human_turn = (board.move_count % 2 == 0 and human_sym == "X") or (board.move_count % 2 == 1 and human_sym == "O")
        if is_human_turn:
                move = board.mouse_click()
                if board.apply_move(move, human_sym):
                    result = board.check_win()
                    if result is not None:
                        if result == 0:
                            print("Draw !")
                        elif (result == 1 and human_sym == "X") or (result == -1 and human_sym == "O"):
                            print("Human Wins !")
                        else:
                            print("Computer Wins !")
                        pygame.time.wait(500)
                        pygame.quit()
                        sys.exit()
        else:
            # Computer Move -> random Move without Intelligence
            pygame.time.wait(500)
            possible_moves = [(r, c) for r in range(1, 4) for c in range(1, 4)]
            unvisited = [m for m in possible_moves if m not in board.visited_cells]
            if unvisited:
                move = random.choice(unvisited)
                if board.apply_move(move, computer_sym):
                    result = board.check_win()
                    if result is not None:
                        if result == 0:
                            print("Draw !")
                        elif (result == 1 and computer_sym == "X") or (result == -1 and computer_sym == "O"):
                            print("Computer Wins !")
                        else:
                            print("Human Wins !")
                        pygame.time.wait(500)
                        pygame.quit()
                        sys.exit()

def HvsH():
    board.board_ui()
    pygame.display.flip()
    while True:
        move = board.mouse_click()
        current_player = "X" if board.move_count % 2 == 0 else "O"
        if board.apply_move(move, current_player):
            result = board.check_win()
            if result is not None:
                if result == 0:
                    print("Draw !")
                elif result == 1:
                    print("X wins !!")
                else:
                    print("O wins !!")
                pygame.time.wait(500)
                pygame.quit()
                sys.exit()
        else:
            print("Invalid Move, Try again !")

CvsH()