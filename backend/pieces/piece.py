

class Piece:
    """
    Pieces know which player they belong to.
    They also have a ref to the board and their position so they can check if a move is legal
    TODO: Having a ref to the board might be circuitous -- could lead to import problems
    """

    def __init__(self, pos, player, board):
        self.position = pos
        self.player = player
        self.board = board

    def get_moves(self):
        raise NotImplementedError

    def check_move(self, move):
        raise NotImplementedError

    def move_piece(self, move):
        raise NotImplementedError