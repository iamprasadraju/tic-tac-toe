from board import Board
import random
import pygame
import sys

board = Board()

def check_win():
    A = set(board.playerA_moves)
    B = set(board.playerB_moves)

    for line in board.win_moves:
        if set(line).issubset(A):
            return 1 # player A wins
        elif set(line).issubset(B):
            return -1 # Player B wins
    if board.move_count >= 9:
        return 0 # Draw 
    return None



def compter_vs_human():
    seq = ["X", "O"]
    human_sym = random.choice(seq)
    computer_sym = "O" if human_sym == "X" else "X"

    board.board_ui()
    pygame.display.flip()
    running = True

    while running:
        # Human move

        is_huamn_turn = (board.move_count % 2 == 0 and human_sym == "X") or (board.move_count % 2 == 1 and human_sym == "O")
        if is_huamn_turn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and board.move_count < 9:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    row = mouseY // board.CELL_SIZE
                    col = mouseX // board.CELL_SIZE
                    move = (row + 1, col + 1)
                    if board.apply_move(move, human_sym):
                        result = check_win()
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
                    result = check_win()
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

compter_vs_human()
    



