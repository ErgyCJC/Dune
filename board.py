class Board:

    def __init__(self, side_length: int = 16):
        self.side_length = side_length
        self.board = [[None for j in range(self.side_length)] for i in range(self.side_length)]

    def set_unit(self, x: int, y: int, unit):
        self.board[x][y] = unit

    def remove_unit(self, x: int, y: int):
        self.board[x][y] = None

    def get_size(self):
        return self.side_length
