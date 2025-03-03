from core.board import Board
from exceptions import *
from exceptions.exceptions import OutOfBoundsExceptions
from core.color_class import Color



class Player:
    def __init__(self,board: Board,color:int):
        self.__color = color
        self.__board = board


    @property
    def color(self):
        return self.__color

    def make_move(self,board :Board , column: int):

        try:
            self.__board.place_disc(column,self.__color)
            return True
        except OutOfBoundsExceptions:
            return False

    def __str__(self):
        """
        Return a string representation of the computer player, including its color.
        """
        return f"Human Player (Color: {Color.to_string(self.__color)})"

