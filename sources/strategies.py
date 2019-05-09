import random
from board import *
from command import *


""" Классы игровых стратегий """


class Strategy:
    def __init__(self):
        pass

    def produce_turn(self):
        pass


class RobotStrategy (Strategy):
    def produce_turn(self, board: Board, units_costs: dict):
        melange = board.get_harkonnen_melange()

        rnd_number = random.random()
        turn_choice = None
        if rnd_number > 0.5:
            turn_choice = 'attack'
        else:
            turn_choice = 'create'

        if board.is_full() or melange < min(units_costs.values()):
            turn_choice = 'attack'

        if turn_choice == 'attack':
            units = []
            for x in range(board.side_length):
                for y in range(board.side_length):
                    tmp_unit = board.get_unit(x, y)
                    if tmp_unit is not None and hasattr(tmp_unit, 'attack') and tmp_unit.fraction == Fractions().Harkonnen():
                        units.append(tmp_unit)

            if units == []:
                return ['empty', EmptyCommand(board)]
            
            random.shuffle(units)
            attacker = units[0].get_coords()

            units = []
            for x in range(board.side_length):
                for y in range(board.side_length):
                    tmp_unit = board.get_unit(x, y)
                    if tmp_unit is not None and hasattr(tmp_unit, 'health') and tmp_unit.fraction == Fractions().Fremen():
                        units.append(tmp_unit)

            random.shuffle(units)
            enemy = units[0].get_coords()

            return ['attack', AttackCommand(board), attacker + enemy]

        elif turn_choice == 'create':
            x, y = 0, 0
            
            while x + y + 1 < board.side_length or board.is_unit(x, y):
                x = random.randint(0, board.side_length - 1)
                y = random.randint(0, board.side_length - 1)

            war_unit_flag = True
            rnd_number = random.random()
            if rnd_number > 0.7:
                war_unit_flag = False

            if melange == units_costs['war_unit']:
                war_unit_flag = True

            if war_unit_flag:
                rnd_number = random.random()
                if rnd_number > 0.5:
                    unit_type = 'flyer'
                else:
                    unit_type = 'division'
            else:
                unit_type = 'harvester'

            return ['create', CreatingCommand(board), x, y, unit_type]
