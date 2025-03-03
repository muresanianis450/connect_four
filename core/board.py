from connect_four.exceptions.exceptions import OutOfBoundsExceptions, ColumnFilled


#creating a board with 6 rows and 7 columns, np.zeros creates me a matrix 6X7
class Board:
    def __init__(self,rows = 6, columns = 7):
        self.__rows = rows
        self.__columns = columns
        self._board = [[' ' for _ in range(self.__columns)] for _ in range(self.__rows)]

    @property
    def columns(self):
        return self.__columns

    @property
    def rows(self):
        return self.__rows

    def add_element(self,row,column,value):
        self._board[row][column] = value
        return self._board

    def get_element(self,row,column):
        return self._board[row][column]




#place element on the last available row of my input column (just like the game)
    def place_disc(self,column,color): #TODO implement a class for the elements
        if not (0<=column < self.__columns):
            raise OutOfBoundsExceptions()
        if self._board[0][column] != ' ':
            raise ColumnFilled()

        i = 0
        while i < self.__rows and self._board[i][column] == ' ':
            i += 1
        # Place the element in the last empty row
        self._board[i - 1][column] = color
        #print(f"Element placed successfully on row {i-1} and column {column}")

    def __getitem__(self, item):
        return self._board[item]

    @staticmethod
    def _colorize(element):
        """
        Map elements to their corresponding colors for display.
        """
        color_map = {
            1: "\033[91m●\033[0m",  # RED
            2: "\033[92m●\033[0m",  # GREEN
            3: "\033[94m●\033[0m",  # BLUE
            4: "\033[95m●\033[0m",  # PINK
            5: "\033[93m●\033[0m",  # YELLOW
            6: "\033[97m●\033[0m",  # WHITE (computer's default color)
            ' ': ' '  # Empty space
        }
        return color_map.get(element, "NJ")  # Return space for unknown values

    def undo_move(self, col):
        """
        Undo the last move in the given column.
        Removes the topmost non-empty disc from the column.
        :param col: The column where the last move is to be undone.
        """
        for row in range(self.__rows):
            if self._board[row][col] != ' ':
                self._board[row][col] = ' '  # Reset the topmost non-empty cell
                break


    def __str__(self):
        """
        Render the board with colorized elements.
        """
        header = ' ' + ' '.join(str(i) for i in range(self.__columns))
        board_rows = []
        for row in self._board:
            colored_row = ' ' +' '.join(self._colorize(cell) for cell in row)
            board_rows.append(colored_row)
        return header + '\n' + '\n'.join(board_rows) + '\n' + header

    def check_victory(self, color):
        """
        Check if the given color has achieved a victory.
        :param color: The color of the current player (integer).
        :return: True if the player has won, False otherwise.
        """
        # Horizontal check
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if all(self.get_element(row, col + i) == color for i in range(4)):
                    return True

        # Vertical check
        for row in range(self.rows - 3):
            for col in range(self.columns):
                if all(self.get_element(row + i, col) == color for i in range(4)):
                    return True

        # Diagonal Check (down-right)
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if all(self.get_element(row + i, col + i) == color for i in range(4)):
                    return True

        # Diagonal Check (up-right)
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                if all(self.get_element(row - i, col + i) == color for i in range(4)):
                    return True

        return False

    def check_draw(self):
        if all(self.get_element(0,col) != ' ' for col in range(self.columns)):
            return True
        return False

    def is_full(self):
        """
        Check if the board is completely filled.
        """
        return all(self.get_element(0, col) != ' ' for col in range(self.columns))



"""#testing the board
board = Board()
print(board)
board.place_disc(5, '0')
print(board)
"""
"""board = Board()

# Simulating moves
board.place_disc(0, 1)  # Human places a RED disc
board.place_disc(1, 4)  # Computer places a WHITE disc
board.place_disc(1, 1)  # Human places another RED disc

print(board)"""


