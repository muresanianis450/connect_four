from pygame.key import set_text_input_rect

from core.board import Board
from exceptions.exceptions import OutOfBoundsExceptions, ColumnFilled
from random import randint
from core.color_class import Color
from typing import Tuple, Optional

class ComputerPlayer:
    MAX_DEPTH = 10  # Maximum depth for minimax

    WINNING_LINE_SCORE = 1000
    NEAR_WIN_SCORE = 50
    BLOCK_OPPONENT_SCORE = -90
    CENTER_COLUMN_WEIGHT = 3

    def __init__(self, board: Board):
        self._color = 6  # Assuming 6 is the color code for the computer
        self.__board = board

    @property
    def color(self):
        return self._color



    def set_color(self,color):
        self._color = color

    def easy_difficulty(self):
        while True:
            try:
                column = randint(0, self.__board.columns - 1)
                if self.is_valid_move(column):
                    return column
            except OutOfBoundsExceptions:
                continue

    def is_valid_move(self, col):
        """Check if a column has space for a disc."""
        return 0 <= col < self.__board.columns and self.__board.get_element(0, col) == ' '

    def undo_move(self, col):
        """Undo the last move in the given column."""
        for row in range(self.__board.rows):
            if self.__board.get_element(row, col) != ' ':
                self.__board.add_element(row, col, ' ')
                break

    def medium_difficulty(self, opponent_color):
        """
        Determine the computer's move:
        1. Try to win.
        2. Block the opponent's win.
        3. Make a random move.
        """
        # Try to win the game
        for col in range(self.__board.columns):
            if self.is_valid_move(col):
                self.__board.place_disc(col, self._color)
                if self.__board.check_victory(self._color):
                    self.undo_move(col)
                    return col
                self.undo_move(col)

        # Try to block the opponent's win
        for col in range(self.__board.columns):
            if self.is_valid_move(col):
                self.__board.place_disc(col, opponent_color)
                if self.__board.check_victory(opponent_color):
                    self.undo_move(col)
                    return col
                self.undo_move(col)

        # Make a random valid move if no immediate win or block is possible
        return self.easy_difficulty()

    def get_opponent_color(self) -> int:
        return 1 if self._color == 6 else 6

    def hard_difficulty(self, depth: int = 3) -> int:
        """
        Use the minimax algorithm with alpha-beta pruning to determine the best move.
        :param depth: Maximum depth to search in the game tree.
        :return: Column number for the best move.
        """
        if depth > self.MAX_DEPTH:
            depth = self.MAX_DEPTH

        opponent_color = self.get_opponent_color()
        try:
            _, column = self.minimax(self.__board, depth, -float("inf"), float("inf"), True, opponent_color)
            if column is not None:
                return column
            else:
                raise RuntimeError("No valid moves available during hard difficulty.")
        except RuntimeError:
            return self.medium_difficulty(opponent_color)

    def minimax(self, board, depth: int, alpha: float, beta: float, maximizing_player: bool, opponent_color: int) -> \
    Tuple[float, Optional[int]]:
        """
        Minimax with alpha-beta pruning.
        """
        if depth == 0 or board.is_full() or board.check_victory(self._color) or board.check_victory(opponent_color):
            return self.evaluate_board(board), None

        valid_moves = [col for col in range(board.columns) if self.is_valid_move(col)]
        if not valid_moves:
            return self.evaluate_board(board), None

        if maximizing_player:
            value = -float("inf")
            best_column = None
            for col in valid_moves:
                board.place_disc(col, self._color)
                if board.check_victory(self._color):
                    board.undo_move(col)
                    return float("inf"), col
                score, _ = self.minimax(board, depth - 1, alpha, beta, False, opponent_color)
                board.undo_move(col)
                if score > value:
                    value = score
                    best_column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value, best_column
        else:
            value = float("inf")
            best_column = None
            for col in valid_moves:
                board.place_disc(col, opponent_color)
                if board.check_victory(opponent_color):
                    board.undo_move(col)
                    return -float("inf"), col
                score, _ = self.minimax(board, depth - 1, alpha, beta, True, opponent_color)
                board.undo_move(col)
                if score < value:
                    value = score
                    best_column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return value, best_column

    def evaluate_board(self, board) -> int:
        """
        Evaluate the board state for the computer player.
        Positive values favor the computer; negative values favor the opponent.
        """
        score = 0

        # Score center column
        center_array = [board.get_element(row, board.columns // 2) for row in range(board.rows)]
        center_count = center_array.count(self._color)
        score += center_count * self.CENTER_COLUMN_WEIGHT

        # Score horizontal, vertical, and diagonal windows
        for row in range(board.rows):
            for col in range(board.columns - 3):
                window = [board.get_element(row, col + i) for i in range(4)]
                score += self.score_window(window, self._color)

        for col in range(board.columns):
            for row in range(board.rows - 3):
                window = [board.get_element(row + i, col) for i in range(4)]
                score += self.score_window(window, self._color)

        for row in range(board.rows - 3):
            for col in range(board.columns - 3):
                window = [board.get_element(row + i, col + i) for i in range(4)]
                score += self.score_window(window, self._color)

        for row in range(board.rows - 3):
            for col in range(board.columns - 3):
                window = [board.get_element(row + 3 - i, col + i) for i in range(4)]
                score += self.score_window(window, self._color)

        return score

    def score_window(self, window, color) -> int:
        """
        Score a window of 4 cells.
        """
        opponent_color = self.get_opponent_color()
        score = 0

        if window.count(color) == 4:
            score += self.WINNING_LINE_SCORE
        elif window.count(color) == 3 and window.count(" ") == 1:
            score += self.NEAR_WIN_SCORE
        elif window.count(color) == 2 and window.count(" ") == 2:
            score += 10

        if window.count(opponent_color) == 4:
            score -= self.WINNING_LINE_SCORE
        elif window.count(opponent_color) == 3 and window.count(" ") == 1:
            score -= self.WINNING_LINE_SCORE * 2
        elif window.count(opponent_color) == 2 and window.count(" ") == 2:
            score -= 30

        return score

    def __str__(self):
        """
        Return a string representation of the computer player, including its color.
        """
        return f"Computer Player (Color: {Color.to_string(self._color)})"