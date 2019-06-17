from pieces.piece import Piece
from position import Position
from board import Board

class Pawn(Piece):

    def __init__(self, pos: Position, player: int, board: Board):
        Piece.__init__(self, pos, player, board)

    def get_moves(self):
        moves = []
        try:
            forward = Position(self.position.x, self.position.y + 1)
            right = Position(self.position.x + 1, self.position.y + 1)
            left = Position(self.position.x - 1, self.position.y + 1)
        except ValueError:  # Off the board (although shouldn't be possible with a pawn)
            return []

        if not self.board.check_position(forward):
            moves.append(forward)

        if self.board.check_position(right):
            if self.board.get_piece_at_position(right).player != self.player:
                moves.append(right)

        if self.board.check_position(left):
            if self.board.get_piece_at_position(left).player != self.player:
                moves.append(left)

        return moves


    def check_move(self, move):
        pass


    def move_piece(self, move: Position):
        self.position = move

