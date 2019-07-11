from backend.board import Board
from backend.position import Position

class Game:

    def __init__(self, player1: str, player2: str):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        pass

    def check_move(self, player: str, pos1: Position, pos2: Position):
        """
        Check if a move is a valid move
        :param player: Player who moves
        :param pos1: Position of piece to move
        :param pos2: Possible place to move
        :return: Boolean
        """
        pass

    def move_piece(self, player: str, pos1: Position, pos2: Position):
        """
        M
        :param player: Player who moves
        :param pos1: Position of piece to move
        :param pos2: Possible place to move
        :return: Boolean, True if piece was moved, False if move was illegal
        """

    def check_for_win(self):
        """
        Check if the game is over
        :return: player string, None if no one has won
        """
        pass

    def get_board_rep(self):
        """
        :return: Matrix representation of the board used to draw on the frontend
        """

    def upgrade_piece(self, player, pos:Position):
        """
        Upgrade piece at position pos if there is a piece there and it belongs to the correct player
        :param pos:
        :return: Boolean based on if the upgrade happened
        """