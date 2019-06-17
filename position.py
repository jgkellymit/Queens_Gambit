from parameters import BOARD_SIZE

class Position:

    def __init__(self, x: int, y: int):
        # Error handling
        if x > BOARD_SIZE - 1 or y > BOARD_SIZE - 1:
            raise ValueError("Position not in board")
        if x < 0 or y < 0:
            raise ValueError("Position not in board")

        self.x = x
        self.y = y

    def to_string(self):
        return str(self.x) + "_" + str(self.y)

