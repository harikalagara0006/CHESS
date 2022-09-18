from abc import ABC
from .pawn1 import Pawn1
from .pawn2 import Pawn2
from .Pawn3 import Pawn3
from .pawn4 import Pawn4
from .pawn5 import Pawn5


class Piece(ABC):
    BLACK = "black"
    WHITE = "white"

    def __init__(self, position: ChessPosition, color):
        self._position = position
        self._color = color

    @property
    def position(self):
        return self._position

    @property
    def color(self):
        return self._color

    def move(self, target_position):
        self._position = target_position

    def get_threatened_positions(self, board):
        raise NotImplementedError

    def get_moveable_positions(self, board):
        raise NotImplementedError

    def symbol(self):
        black_color_prefix = '\u001b[31;1m'
        white_color_prefix = '\u001b[34;1m'
        color_suffix = '\u001b[0m'
        retval = self._symbol_impl()
        if self.color == Piece.BLACK:
            retval = black_color_prefix + retval + color_suffix
        else:
            retval = white_color_prefix + retval + color_suffix
        return retval

    def _symbol_impl(self):
        raise NotImplementedError

class PieceFactory:
    @staticmethod
    def create(piece_type: str, position: ChessPosition, color):
        if piece_type == PieceType.pawn1:
            return pawn1(position, color)
        
        if piece_type == PieceType.PAWN3:
            return pawn3(position, color)
        
        if piece_type == PieceType.PAWN2:
            return pawn2(position, color)
        
        if piece_type == PieceType.PAWN4:
            return pawn4(position, color)
        
        if piece_type == PieceType.PAWN5:
            return pawn5(position, color)
        
        if piece_type == PieceType.PAWN:
            return Pawn(position, color)