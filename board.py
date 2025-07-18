import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

class Board():
    def __init__(self, draw_enabled = True):
        self.font = pygame.font.SysFont('Corbel', 35)
        self.button_font = pygame.font.SysFont('Corbel', 25)

        self.button_cvsh = pygame.Rect(WIDTH//2 - 150, HEIGHT//2, 300, 50)
        self.button_hvsh = pygame.Rect(WIDTH//2 - 150, HEIGHT//2 + 70, 300, 50)


        self.draw_enabled = draw_enabled

        self.LINE_COLOR = (255, 255, 255)
        self.LINE_WIDTH = 2
        self.CELL_SIZE = WIDTH // 3

        self.visited_cells = []
        self.playerA_moves = []  # X
        self.playerB_moves = []  # O
        self.move_count = 0

        # Create winning positions
        board_positions = [[(i, j) for j in range(1, 4)] for i in range(1, 4)]
        vertical_positions = [[board_positions[row][col] for row in range(3)] for col in range(3)]
        horizontal_positions = board_positions
        diagonal_positions = [
            [board_positions[i][i] for i in range(3)],
            [board_positions[i][2 - i] for i in range(3)]
        ]

        self.win_moves = vertical_positions + horizontal_positions + diagonal_positions

    def board_ui(self):
        screen.fill((0, 0, 0))  # Black background

        # Draw grid
        pygame.draw.line(screen, self.LINE_COLOR, (self.CELL_SIZE, 0), (self.CELL_SIZE, HEIGHT), self.LINE_WIDTH)
        pygame.draw.line(screen, self.LINE_COLOR, (2 * self.CELL_SIZE, 0), (2 * self.CELL_SIZE, HEIGHT), self.LINE_WIDTH)
        
        pygame.draw.line(screen, self.LINE_COLOR, (0, self.CELL_SIZE), (WIDTH, self.CELL_SIZE), self.LINE_WIDTH)
        pygame.draw.line(screen, self.LINE_COLOR, (0, 2 * self.CELL_SIZE), (WIDTH, 2 * self.CELL_SIZE), self.LINE_WIDTH)

    def draw_circle(self, row, col):
        center_x = col * self.CELL_SIZE + self.CELL_SIZE // 2
        center_y = row * self.CELL_SIZE + self.CELL_SIZE // 2
        radius = self.CELL_SIZE // 3
        pygame.draw.circle(screen, self.LINE_COLOR, (center_x, center_y), radius, self.LINE_WIDTH)

    def draw_cross(self, row, col):
        padding = 33
        start_x = col * self.CELL_SIZE + padding
        start_y = row * self.CELL_SIZE + padding
        end_x = (col + 1) * self.CELL_SIZE - padding
        end_y = (row + 1) * self.CELL_SIZE - padding

        pygame.draw.line(screen, self.LINE_COLOR, (start_x, start_y), (end_x, end_y), self.LINE_WIDTH)
        pygame.draw.line(screen, self.LINE_COLOR, (end_x, start_y), (start_x, end_y), self.LINE_WIDTH)


    def draw_winning_line(self, line):
        # line is a list of 3 moves, e.g. [(1,1), (1,2), (1,3)]
        start_cell = line[0]
        end_cell = line[2]

        # Convert board positions (1-based) to pixel center positions
        start_x = (start_cell[1] - 1) * self.CELL_SIZE + self.CELL_SIZE // 2
        start_y = (start_cell[0] - 1) * self.CELL_SIZE + self.CELL_SIZE // 2

        end_x = (end_cell[1] - 1) * self.CELL_SIZE + self.CELL_SIZE // 2
        end_y = (end_cell[0] - 1) * self.CELL_SIZE + self.CELL_SIZE // 2

        # Draw a thick red line across the winning cells
        pygame.draw.line(screen, (255, 0, 0), (start_x, start_y), (end_x, end_y), 8)
        pygame.display.flip()
        pygame.time.wait(1000)


    def apply_move(self, move, player_symbol):
        if move in self.visited_cells:
            return False

        row, col = move[0] - 1, move[1] - 1
        self.visited_cells.append(move)

        if self.draw_enabled:
            if player_symbol == "X":
                self.draw_cross(row, col)
                pygame.display.set_caption("O Turn!")
            else:
                self.draw_circle(row, col)
                pygame.display.set_caption("X Turn!")
            pygame.display.flip()

        if player_symbol == "X":
            self.playerA_moves.append(move)
        else:
            self.playerB_moves.append(move)

        self.move_count += 1
        return True
    
    def Home_ui(self):
        screen.fill("purple") # Black

        title_surface = self.font.render("Tic Tac Toe", True, (255, 255, 255))
        title_rect = title_surface.get_rect()

        title_rect.center = (WIDTH // 2, HEIGHT // 6)
        screen.blit(title_surface, title_rect)


        # Draw buttons
        pygame.draw.rect(screen, (0, 128, 255), self.button_cvsh)  # Blue button
        pygame.draw.rect(screen, (0, 128, 255), self.button_hvsh)

        # Button text
        cvsh_text = self.button_font.render("Play Computer vs Human", True, (255, 255, 255))
        hvsh_text = self.button_font.render("Play Human vs Human", True, (255, 255, 255))

        cvsh_rect = cvsh_text.get_rect(center = self.button_cvsh.center)
        hvsh_rect = hvsh_text.get_rect(center = self.button_hvsh.center)

        screen.blit(cvsh_text, cvsh_rect)
        screen.blit(hvsh_text, hvsh_rect)


        pygame.display.flip()


    def gameOver_ui(self, winner, human_sym = None):
        screen.fill((255, 100, 100))  # Red background
        if human_sym is None:
            # Message and emoji based on winner
            if winner == 1:  # Player A (X) wins
                message = "X Wins! "
            elif winner == -1:  # Player B (O) wins
                message = "O Wins! "
            else:  # Draw
                message = "Draw! "

        else:
            if winner == 0:
                message = "It's a Draw!"
            
            elif (winner == 1 and human_sym == "X") or (winner == -1 and human_sym == "O"):
                message = "Human Wins!"
            else:
                message = "Computer Wins!"

        # Render message
        msg_surface = self.font.render(message, True, (255, 255, 255))
        msg_rect = msg_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(msg_surface, msg_rect)

        # Restart button rectangle
        self.restart_button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2, 200, 50)
        pygame.draw.rect(screen, (0, 128, 255), self.restart_button)

        # Restart button text
        restart_text = self.button_font.render("Restart Game", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=self.restart_button.center)
        screen.blit(restart_text, restart_rect)

        pygame.display.flip()

        pygame.time.wait(500)



    def handle_home_events(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_cvsh.collidepoint(event.pos):
                        return "CvsH"  # Computer vs Human selected
                    elif self.button_hvsh.collidepoint(event.pos):
                        return "HvsH"  # Human vs Human selected

            self.Home_ui()


    def mouse_click(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and self.move_count < 9:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    row = mouseY // self.CELL_SIZE
                    col = mouseX // self.CELL_SIZE
                    move = (row + 1, col + 1)
                    return move
                    
    def get_available_moves(self):
        all_moves = [(i, j) for i in range(1, 4) for j in range(1, 4)]
        return [move for move in all_moves if move not in self.visited_cells]
    
    def check_win(self):
        A = set(self.playerA_moves)
        B = set(self.playerB_moves)

        for line in self.win_moves:
            if set(line).issubset(A):
                return 1, line  # player A wins + winning line
            elif set(line).issubset(B):
                return -1, line  # player B wins + winning line
        if self.move_count == 9:
            return 0, None
        return None, None
    
    def reset(self):
        self.visited_cells = []
        self.playerA_moves = []
        self.playerB_moves = []
        self.move_count = 0
        self.board_ui()
        pygame.display.flip()
