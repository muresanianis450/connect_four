import sys
from connect_four.core.board import Board
from connect_four.core.player import Player
from connect_four.core.computer import ComputerPlayer
from connect_four.core.color_class import Color
from connect_four.exceptions.exceptions import ColumnFilled, OutOfBoundsExceptions
from connect_four.application.game_manager import ConnectFourApp

# Constants for player colors
COLOR_OPTIONS = {
    1: Color.RED,
    2: Color.GREEN,
    3: Color.BLUE,
    4: Color.PINK,
    5: Color.YELLOW
}


class UI:
    def __init__(self):
        """
        Initialize the UI and the game manager.
        """
        self._game = ConnectFourApp()

    @staticmethod
    def display_welcome():
        """
        Display a welcome message.
        """
        print("Welcome to Connect Four!")
        print("Get ready to drop your discs and connect four in a row!")

    def display_board(self):
        """
        Display the current state of the board.
        """
        print("\nCurrent Board:")
        print(self._game.board)

    def display_turn_prompt(self):
        """
        Display a prompt for the current player's turn.
        """
        current_player = self._game.current_player
        if isinstance(current_player, Player):
            print(f"It's your turn! You are {Color.to_string(current_player.color)}.")
        else:
            print("Computer is making its move...")

    def display_winner(self):
        """
        Display the winner or draw message.
        """
        if isinstance(self._game.current_player, Player):
            print("Congratulations! You won! :)")
        else:
            print("The computer won. Better luck next time!")
        print("Game Over.")

    def display_draw(self):
        """
        Display a draw message.
        """
        print("It's a draw! Well played!")
        print("Game Over.")

    def get_player_preferences(self):
        """
        Get player color and difficulty from the user.
        """
        print("Choose your color: 1-Red, 2-Green, 3-Blue, 4-Pink, 5-Yellow")
        color_choice = int(input("Enter the number corresponding to your color choice: "))
        player_color = COLOR_OPTIONS[color_choice]

        print("Choose difficulty: 1-Easy, 2-Medium, 3-Hard")
        difficulty = int(input("Enter the number corresponding to your difficulty choice: "))
        return player_color, difficulty

    def run(self):
        """
        Main method to run the game.
        """
        self.display_welcome()
        player_color, difficulty = self.get_player_preferences()
        self._game.setup_game(player_color, difficulty)

        while self._game.is_running:
            self.display_board()
            self.display_turn_prompt()
            self._game.play_turn()
            self._game.check_game_over()

            if self._game.is_running:
                self._game.switch_player()

        # Game over state
        self.display_board()
        if self._game.check_draw():
            self.display_draw()
        else:
            self.display_winner()


