class BoardException(Exception):
    def __init__(self, message):
        self.__message = message
    def __str__(self):
        return self.__message
class OutOfBoundsExceptions(BoardException):
    def __init__(self):
        super().__init__("That position is out of bounds!")

class ColumnFilled(BoardException):
    def __init__(self):
        super().__init__("Column is full!")