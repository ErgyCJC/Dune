from board import *
from units import *
from military_structure import *


""" Вывод игровой доски в терминал """


class Drawer:
    def __init__(self, board: Board):
        self.board = board

    def draw(self, turn: int, melange: int):
        size = self.board.side_length

        # White text with black background
        print('\033[1;37;40m', end='')

        print('\n\nTurn:', turn, '| Melange:', melange, end='\n\n')

        print(' ' * 3, end='')
        for x in range(size):
            print(x, end=' ')
            if x < 10:
                print(end=' ')
        print('')

        for y in range(size):
            if y < 10:
                print(str(y), end='  ')
            else:
                print(str(y), end=' ')

            for x in range(size):
                unit = self.board.get_unit(x, y)

                if unit is None:
                    print('\033[1;30;40m' + '.', end='')
                else:
                    # Set cyan text - Fremen color
                    if unit.fraction is Fractions().Fremen():
                        print('\033[1;36;40m', end='')
                    # Set red color - Harkonnen color
                    else:
                        print('\033[1;31;40m', end='')

                    if isinstance(unit, Flyer):
                        print('%', end='')
                    elif isinstance(unit, Division) or isinstance(unit, WarriorsUnion):
                        print('*', end='')
                    elif isinstance(unit, MotherBaseUnit):
                        print('@', end='')

                if x < 10:
                    print(end=' ')

                # White text
                print('\033[1;37;40m', end='')

                if x < 10:
                    print(' ', end='')
                else:
                    print('  ', end='')
                    
            print('\n', end='')