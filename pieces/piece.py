

class Piece:

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