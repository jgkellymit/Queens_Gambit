from backend.pieces.piece import Piece
from backend.position import Position
from backend.parameters import BOARD_SIZE
from typing import Dict


class Board:

    def __init__(self):
        self.board_size: int = BOARD_SIZE
        # self.board: Dict[str, Piece] = {}  # Dictionary representation of the board, including what pieces are where
        # for y in range(self.board_size):
        #     for x in range(self.board_size):
        #         self.board[str(x) + "_" + str(y)] = None
        self.board: Dict[Position, Piece] = {}  # Dictionary representation of the board, including what pieces are where

    def check_position(self, pos: Position):
        """Return True if there is a piece at the given Position, otherwise return False"""
        if self.board[pos.to_string()] is None:
            return False

        return True

    def get_piece_at_position(self, pos: Position):
        """Get the piece at a specific position"""
        return self.board[pos.to_string()]

    def place_piece(self, pos: Position, piece: Piece):
        """Put a piece at a given position, return None"""
        self.board[pos] = piece
        print("PLACED PIECE")
        print(self.board)

    def check_for_win(self):
        """Check if the game is over"""
        pass

    def check_if_move_is_valid(self, pos1, pos2):
        """Check if a given move is valid"""
        pass

    def upgrade_piece(self, player: str, pos: Position):
        """Upgrade piece at given position, return boolean"""
        pass





if __name__ == '__main__':
    print("2")