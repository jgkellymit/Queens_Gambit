from pieces.piece import Piece
from position import Position
from parameters import BOARD_SIZE
from typing import Dict


class Board:

    def __init__(self):
        self.board_size: int = BOARD_SIZE
        self.board: Dict[str, Piece] = {}
        for y in range(self.board_size):
            for x in range(self.board_size):
                self.board[str(x) + "_" + str(y)] = None


    def check_position(self, pos: Position):
        if self.board[pos.to_string()] is None:
            return False

        return True

    def get_piece_at_position(self, pos: Position):
        return self.board[pos.to_string()]


    def place_piece(self, piece: Piece, position: Position):
        self.board[position.to_string()] = piece




if __name__ == '__main__':
    print("2")