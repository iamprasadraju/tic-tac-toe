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
                return 1 # player A wins
            elif set(line).issubset(B):
                return -1 # Player B wins
        if self.move_count == 9:
            return 0 # Draw 
        return None
    
    def reset(self):
        self.visited_cells = []
        self.playerA_moves = []
        self.playerB_moves = []
        self.move_count = 0
        self.board_ui()
        pygame.display.flip()
