from units import *
from decorators import *


class Board:

    def __init__(self, side_length: int = 16):
        self.side_length = side_length
        self.board = [[None for j in range(self.side_length)] for i in range(self.side_length)]
        
        self.filled_count = 0
        self.fremen_melange = 10
        self.harkonnen_melange = 10

    def set_unit(self, x: int, y: int, unit, replace = False) -> bool:
        if self.valid_coords(x, y):
            
            if replace or not self.is_unit(x, y):
                self.board[x][y] = unit
                self.recalc_filled_count()
                
                return True

        return False

    def remove_unit(self, x: int, y: int):
        self.board[x][y] = None
        self.filled_count -= 1

    def get_unit(self, x: int, y: int):
        return self.board[x][y]

    def get_harkonnen_melange(self) -> int:
        return self.harkonnen_melange

    def get_fremen_melange(self) -> int:
        return self.fremen_melange

    def change_harkonnen_melange(self, delta: int):
        self.harkonnen_melange += delta

    def change_fremen_melange(self, delta: int):
        self.fremen_melange += delta

    def get_size(self):
        return self.side_length

    def is_unit(self, x: int, y: int):
        return not self.board[x][y] is None

    def valid_coords(self, x: int, y: int) -> bool:
        return 0 <= x < self.side_length and 0 <= y <= self.side_length

    def move_unit(self, x_from: int, y_from: int, x_to: int, y_to: int) -> bool:
        if self.valid_coords(x_from, y_from) and self.valid_coords(x_to, y_to):
            
            if self.board[x_from][y_from] is not None and self.board[x_to][y_to] is None:
                self.board[x_to][y_to] = self.board[x_from][y_from]
                self.board[x_from][y_from] = None
                return True

            return False
        
        return False

    def recalc_filled_count(self) -> int:
        count = 0

        for x in range(self.side_length):
            for y in range(self.side_length):
                if self.get_unit(x, y) is not None:
                    count += 1

        self.filled_count = count
        return self.filled_count

    def is_full(self):
        return self.filled_count == int(self.side_length ** 2)

    def earn_melange(self):
        for x in range(self.side_length):
            for y in range(self.side_length):
                unit = self.get_unit(x, y)
                if isinstance(unit, MotherBaseUnit):

                    if unit.fraction == Fractions().Fremen():
                        self.fremen_melange += unit.get_melange()
                    elif unit.fraction == Fractions().Harkonnen():
                        self.harkonnen_melange += unit.get_melange()

    def update_board(self):
        for x in range(self.side_length):
            for y in range(self.side_length):
                
                unit = self.get_unit(x, y)
                if unit is not None:
                    if hasattr(unit, 'health') and unit.health <= 0:
                        self.set_unit(x, y, None, True)

                    if hasattr(unit, 'reconstructing_turns'):
                        if unit.reconstructing_turns == 0:
                            decorator = ReconstructedDecorator()
                            unit = decorator(unit)
                        else:
                            unit.reconstructing_turns -= 1
                        self.set_unit(x, y, unit, True)