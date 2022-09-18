from .pieces import Piece


class Pawn3(Piece):
    SPOT_INCREMENTS_MOVE = [(0, 1)]
    SPOT_INCREMENTS_MOVE_FIRST = [(0, 1), (0, 2)]
    SPOT_INCREMENTS_TAKE = [(-1, 1), (1, 1)]

    def __init__(self, position: ChessPosition, color: str):
        super().__init__(position, color)
        self._moved = False

    def get_threatened_positions(self, board):
        positions = []
        increments = Pawn3.SPOT_INCREMENTS_TAKE
        for increment in increments:
            positions.append(board.spot_search_threat(self._position, self._color, increment[0], increment[1] if self.color == Piece.WHITE else (-1) * increment[1]))
        positions = [x for x in positions if x is not None]
        return positions

    def get_moveable_positions(self, board):
        positions = []
        increments = Pawn3.SPOT_INCREMENTS_MOVE if self._moved else Pawn3.SPOT_INCREMENTS_MOVE_FIRST
        for increment in increments:
            positions.append(board.spot_search_threat(self._position, self._color, increment[0], increment[1] if self.color == Piece.WHITE else (-1) * increment[1], free_only=True))

        increments = Pawn3.SPOT_INCREMENTS_TAKE
        for increment in increments:
            positions.append(board.spot_search_threat(self._position, self._color, increment[0], increment[1] if self.color == Piece.WHITE else (-1) * increment[1], threat_only=True))

        positions = [x for x in positions if x is not None]
        return positions

    def move(self, target_position):
        self._moved = True
        Piece.move(self, target_position)

    def _symbol_impl(self):
        return 'PA3'