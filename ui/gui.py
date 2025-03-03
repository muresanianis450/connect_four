import pygame
import sys
import os
from core.board import Board
from core.player import Player
from core.computer import ComputerPlayer
from core.color_class import Color
from exceptions.exceptions import ColumnFilled, OutOfBoundsExceptions

# Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
CELL_SIZE = 100
RADIUS = CELL_SIZE // 2 - 5
FONT_SIZE = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (169, 169, 169)

# Player Colors
COLOR_OPTIONS = {
    1: RED,
    2: GREEN,
    3: BLUE,
    4: (255, 105, 180),  # Pink
    5: YELLOW
}

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize the mixer for playing sounds



#Sound no more valid, please add a path in order to use sound in your code
"""# Correct file paths (use double backslashes or forward slashes)
WIN_SOUND_PATH = "C:/Users/mures/OneDrive/2024 dump/Documents/GitHub/a10-muresanianis450/win_sound.wav"
LOSE_SOUND_PATH = "C:/Users/mures/OneDrive/2024 dump/Documents/GitHub/a10-muresanianis450/loose_sound.wav"""

"""# Validate sound file paths
if not os.path.exists(WIN_SOUND_PATH) or not os.path.exists(LOSE_SOUND_PATH):
    print("Sound files are missing. Ensure paths are correct.")
    sys.exit()"""

"""# Load sounds with error handling
try:
    win_sound = pygame.mixer.Sound(WIN_SOUND_PATH)
    lose_sound = pygame.mixer.Sound(LOSE_SOUND_PATH)
except pygame.error as e:
    print(f"Error loading sound files: {e}")
    sys.exit()"""

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Connect Four")

# Fonts
font = pygame.font.SysFont("monospace", FONT_SIZE)


class ConnectFourGUI:
    def __init__(self):
        self.board = Board()
        self.human_player = None
        self.computer_player = None
        self.current_player = None
        self.difficulty = None
        self.is_running = True
        self.game_over = False

    def setup_game(self, player_color, difficulty):
        """
        Set up the game: assign colors and initialize players.
        """
        self.human_player = Player(self.board, player_color)
        self.computer_player = ComputerPlayer(self.board)
        self.computer_player.set_color(WHITE)  # Set computer player color to white
        self.current_player = self.human_player
        self.difficulty = difficulty

    def play_turn(self, column):
        """
        Handle the human player's turn.
        """
        try:
            self.board.place_disc(column, self.current_player.color)
            return True
        except (ColumnFilled, OutOfBoundsExceptions):
            return False

    def computer_turn(self):
        """
        Handle the computer's turn.
        """
        try:
            if self.difficulty == 1:
                column = self.computer_player.easy_difficulty()
            elif self.difficulty == 2:
                column = self.computer_player.medium_difficulty(self.human_player.color)
            elif self.difficulty == 3:
                column = self.computer_player.hard_difficulty()
            self.board.place_disc(column, self.computer_player.color)
        except (ColumnFilled, OutOfBoundsExceptions):  # Handle errors gracefully
            pass

    def switch_player(self):
        """
        Switch the current player between the human and computer.
        """
        self.current_player = (
            self.computer_player if self.current_player == self.human_player else self.human_player
        )

    def check_game_over(self):
        """
        Check if the game has ended with a win or draw.
        """
        if self.board.check_victory(self.current_player.color):
            self.game_over = True
            return True
        if self.board.is_full():
            self.game_over = True
            return False
        return False


def draw_board(board, human_color, computer_color):
    """
    Draw the Connect Four board on the screen.
    """
    vertical_offset = (SCREEN_HEIGHT - (board.rows * CELL_SIZE)) // 2
    for row in range(board.rows):
        for col in range(board.columns):
            pygame.draw.rect(
                screen,
                GREY,
                (col * CELL_SIZE, vertical_offset + row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )
            pygame.draw.circle(
                screen,
                BLACK,
                (col * CELL_SIZE + CELL_SIZE // 2, vertical_offset + row * CELL_SIZE + CELL_SIZE // 2),
                RADIUS,
            )
    for row in range(board.rows):
        for col in range(board.columns):
            if board.get_element(row, col) == human_color:
                pygame.draw.circle(
                    screen,
                    human_color,
                    (col * CELL_SIZE + CELL_SIZE // 2, vertical_offset + row * CELL_SIZE + CELL_SIZE // 2),
                    RADIUS,
                )
            elif board.get_element(row, col) == computer_color:
                pygame.draw.circle(
                    screen,
                    computer_color,
                    (col * CELL_SIZE + CELL_SIZE // 2, vertical_offset + row * CELL_SIZE + CELL_SIZE // 2),
                    RADIUS,
                )
    pygame.display.update()


def show_menu():
    """
    Display the menu to choose player color and difficulty.
    """
    screen.fill(WHITE)
    title = font.render("Connect Four", True, BLACK)
    screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 50))

    color_text = font.render("Choose your color:", True, BLACK)
    screen.blit(color_text, (50, 150))
    color_buttons = []
    for i, (color_code, color) in enumerate(COLOR_OPTIONS.items(), start=1):
        color_button = pygame.Rect(50, 150 + i * 40, 200, 30)
        pygame.draw.rect(screen, color, color_button)
        color_label = font.render(f"{Color.to_string(color_code)}", True, BLACK)
        screen.blit(color_label, (60, 150 + i * 40))
        color_buttons.append((color_button, color))

    difficulty_text = font.render("Choose difficulty:", True, BLACK)
    screen.blit(difficulty_text, (50, 400))
    difficulty_buttons = []
    for i, difficulty in enumerate(["Easy", "Medium", "Hard"], start=1):
        difficulty_button = pygame.Rect(50, 400 + i * 40, 200, 30)
        pygame.draw.rect(screen, BLACK, difficulty_button)
        difficulty_label = font.render(difficulty, True, WHITE)
        screen.blit(difficulty_label, (60, 400 + i * 40))
        difficulty_buttons.append((difficulty_button, i))

    pygame.display.update()

    player_color = None
    difficulty = None

    while player_color is None or difficulty is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for button, color in color_buttons:
                    if button.collidepoint(mouse_pos):
                        player_color = color
                for button, diff in difficulty_buttons:
                    if button.collidepoint(mouse_pos):
                        difficulty = diff

    return player_color, difficulty


def main():
    # Show menu to get player preferences
    player_color, difficulty = show_menu()

    # Initialize game
    game = ConnectFourGUI()
    game.setup_game(player_color=player_color, difficulty=difficulty)

    running = True
    while running:
        draw_board(game.board, game.human_player.color, game.computer_player.color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
                pos_x = event.pos[0]
                col = pos_x // CELL_SIZE
                if 0 <= col < game.board.columns:  # Ensure column is valid
                    if game.play_turn(col):
                        if game.check_game_over():
                            draw_board(game.board, game.human_player.color, game.computer_player.color)
                            pygame.mixer.stop()
                            #pygame.mixer.Sound.play(win_sound)
                        else:
                            game.switch_player()

        if game.current_player == game.computer_player and not game.game_over:
            pygame.time.wait(500)  # Simulate thinking
            game.computer_turn()
            if game.check_game_over():
                draw_board(game.board, game.human_player.color, game.computer_player.color)
                pygame.mixer.stop()
                #pygame.mixer.Sound.play(lose_sound)
            else:
                game.switch_player()

        if game.game_over:
            text = "Draw!" if game.board.is_full() else (
                "You Win!" if isinstance(game.current_player, Player) else "Computer Wins!"
            )
            label = font.render(
                text, 1, GREEN if text == "You Win!" else RED
            )
            screen.blit(label, (SCREEN_WIDTH // 2 - label.get_width() // 2, CELL_SIZE // 2))
            pygame.display.update()
            pygame.time.wait(10000)
            running = False


