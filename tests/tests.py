import unittest
from connect_four.core.board import Board
from connect_four.core.player import Player
from connect_four.core.computer import ComputerPlayer
from connect_four.core.color_class import Color
from connect_four.application.game_manager import ConnectFourApp
from connect_four.exceptions.exceptions import ColumnFilled, OutOfBoundsExceptions

class TestConnectFourApp(unittest.TestCase):

    def setUp(self):
        """
        Set up the test case with a ConnectFourApp instance and medium difficulty.
        """
        self.app = ConnectFourApp()
        self.app.setup_game(Color.RED, 2)  # Set up with medium difficulty

    def test_column_filled_exception(self):
        """
        Test that a ColumnFilled exception is raised when placing a disc in a full column.
        """
        for _ in range(self.app.board.rows):
            self.app.board.place_disc(0, Color.RED)
        with self.assertRaises(ColumnFilled):
            self.app.board.place_disc(0, Color.RED)

    def test_out_of_bounds_exception(self):
        """
        Test that an OutOfBoundsExceptions exception is raised when placing a disc out of bounds.
        """
        with self.assertRaises(OutOfBoundsExceptions):
            self.app.board.place_disc(7, Color.RED)

    def test_check_victory_horizontal(self):
        """
        Test that a horizontal victory is correctly identified.
        """
        for col in range(4):
            self.app.board.place_disc(col, Color.RED)
        self.assertTrue(self.app.board.check_victory(Color.RED))

    def test_check_victory_vertical(self):
        """
        Test that a vertical victory is correctly identified.
        """
        for _ in range(4):
            self.app.board.place_disc(0, Color.RED)
        self.assertTrue(self.app.board.check_victory(Color.RED))

    def test_check_victory_diagonal(self):
        """
        Test that a diagonal victory is correctly identified.
        """
        for i in range(4):
            for j in range(i):
                self.app.board.place_disc(i, Color.YELLOW)
            self.app.board.place_disc(i, Color.RED)
        self.assertTrue(self.app.board.check_victory(Color.RED))

    def test_computer_easy_difficulty(self):
        """
        Test that the computer's easy difficulty move is within valid columns.
        """
        self.app.difficulty = 1
        column = self.app.computer_player.easy_difficulty()
        self.assertIn(column, range(self.app.board.columns))

    def test_computer_medium_difficulty(self):
        """
        Test that the computer's medium difficulty move is within valid columns.
        """
        self.app.difficulty = 2
        column = self.app.computer_player.medium_difficulty(Color.RED)
        self.assertIn(column, range(self.app.board.columns))

    def test_computer_hard_difficulty(self):
        """
        Test that the computer's hard difficulty move is within valid columns.
        """
        self.app.difficulty = 3
        column = self.app.computer_player.hard_difficulty()
        self.assertIn(column, range(self.app.board.columns))

