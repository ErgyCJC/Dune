class Board:

    def __init__(self, side_length: int = 16):      
        self.side_length = side_length
        self.board = [[None for j in range(self.side_length)] for i in range(self.side_length)]

    def set_unit(self, x: int, y: int, unit) -> bool:
        if self.valid_coords(x, y) and not self.is_unit(x, y):
            self.board[x][y] = unit
            return True

        return False

    def remove_unit(self, x: int, y: int):
        self.board[x][y] = None

    def get_unit(self, x: int, y: int):
        return self.board[x][y]

    def get_size(self):
        return self.side_length

    def is_unit(self, x: int, y: int):
        return not self.board[x][y] is None

    def valid_coords(self, x: int, y: int) -> bool:
        return 0 <= x < self.side_length and 0 <= y <= self.side_length