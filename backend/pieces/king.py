from backend.pieces.piece import Piece
from backend.position import Position


class King(Piece):

    def __init__(self, pos: Position):
        Piece.__init__(self, pos)

    def get_moves(self):
        return

    def check_move(self, move):
        pass

    def move_piece(self, move):
        pass

