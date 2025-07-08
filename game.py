from board import Board
import random
import pygame
import sys

board = Board()

def compter_vs_human():
    seq = ["X", "O"]
    symbol = random.choice(seq)
    Human = symbol
    seq.remove(symbol)
    computer = seq[0]
    

    board.board_ui()
    pygame.display.flip()
    running = True
    while running:
        # Human move
        if board.move_count % 2 == 0 and Human == "X" or board.move_count % 2 == 1 and Human == "O":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and board.move_count < 9:
                    board.move()
                    if Human == board.check_win():
                        print("Human Wins !")
                        sys.exit()
                    
        else:
            # Computer Move -> random Move without Intelligence
            pygame.time.wait(500)
            possible_moves = [(r, c) for r in range(1, 4) for c in range(1, 4)]
            unvisited = [m for m in possible_moves if m not in board.visited_cells]
            if unvisited:
                move = random.choice(unvisited)
                row, col = move[0] - 1, move[1] - 1
                if board.move_count % 2 == 0:
                    board.draw_cross(row, col)
                    board.playerA_moves.append(move)
                    pygame.display.set_caption("Your Turn!" if Human == "O" else "Computer Thinking...")
                else:
                    board.draw_circle(row, col)
                    board.playerB_moves.append(move)
                    pygame.display.set_caption("Your Turn!" if Human == "X" else "Computer Thinking...")


                board.visited_cells.append(move)
                board.move_count += 1
                pygame.display.flip()
                if computer == board.check_win():
                    print("Computer Wins !")
                    sys.exit()

        if board.move_count >= 9:
            pygame.display.set_caption("It's a Draw!")
            print("It's a Draw!")
            pygame.time.wait(2000)
            running = False


compter_vs_human()