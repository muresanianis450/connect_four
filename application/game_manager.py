from core.player import Player
from core.board import Board
from core.computer import ComputerPlayer
from core.color_class import Color
from exceptions.exceptions import OutOfBoundsExceptions, ColumnFilled
import time

class ConnectFourApp:
    def __init__(self):
        self.board = Board()
        self.human_player = None
        self.computer_player = None
        self.current_player = None
        self.is_running = True
        self.difficulty = None

    def setup_game(self, player_color, difficulty):
        """
        Set up the game: assign colors and initialize players.
        """
        self.human_player = Player(self.board, player_color)
        self.computer_player = ComputerPlayer(self.board)
        self.computer_player.set_color(Color.WHITE)  # Set computer player color to WHITE
        self.current_player = self.human_player
        self.difficulty = difficulty

    def play_turn(self):
        """
        Handle a single turn for the current player.
        """
        if isinstance(self.current_player, Player):
            # Human player's turn
            while True:
                try:
                    column = int(input(f"{Color.to_string(self.current_player.color)}, enter the column (0-6) to drop your disc: "))
                    self.board.place_disc(column, self.current_player.color)
                    break  # Exit the loop once a valid move is made
                except (OutOfBoundsExceptions, ColumnFilled) as e:
                    print(f"Error: {e}. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 6.")
        else:
            # Computer player's turn
            if self.difficulty == 1:
                column = self.computer_player.easy_difficulty()
            elif self.difficulty == 2:
                column = self.computer_player.medium_difficulty(self.human_player.color)
            elif self.difficulty == 3:
                column = self.computer_player.hard_difficulty()

            self.board.place_disc(column, self.computer_player.color)

    def switch_player(self):
        """
        Switch the current player between the human player and the computer player.
        """
        self.current_player = self.computer_player if self.current_player == self.human_player else self.human_player

    def check_game_over(self):
        """
        Check if the game has ended with a win or a draw.
        """
        if self.board.check_victory(self.current_player.color):
            print(self.board)
            if isinstance(self.current_player, Player):
                print("Congratulations! You won! :)")
            else:
                print("The computer won. Better luck next time!")
            self.is_running = False
            return

        if self.board.is_full():
            print(self.board)
            print("The game is a draw!")
            self.is_running = False

    def check_draw(self):
        """
        Check if the game is a draw.
        """
        return self.board.is_full() and not self.board.check_victory(self.human_player.color) and not self.board.check_victory(self.computer_player.color)