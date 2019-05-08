from dune import *
from units import *
from board import *
from decorators import *


class Command:
    def __init__(self, board: Board):
        self.board = board

    def __call__(self):
        pass


class MoveCommand (Command):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self, args: list, fraction: str) -> bool:
        x_from = int(args[0])
        y_from = int(args[1])
        x_to = int(args[2])
        y_to = int(args[3])

        unit = self.board.get_unit(x_from, y_from)
        
        valid_speed_flag = False
        if hasattr(unit, 'speed') and unit.speed > 0:
            valid_speed_flag = True

        if unit is None or unit.fraction is not fraction or not valid_speed_flag:
            return False

        if abs(x_from - x_to) + abs(y_from - y_to) > unit.speed:
            return False

        return self.board.move_unit(x_from, y_from, x_to, y_to)


class AttackCommand (Command):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self, args: list, fraction: str) -> bool:
        x_attacker = int(args[0])
        y_attacker = int(args[1])
        x_enemy = int(args[2])
        y_enemy = int(args[3])
        
        coords_valid_flag = self.board.valid_coords(x_attacker, y_attacker)
        coords_valid_flag = coords_valid_flag and self.board.valid_coords(x_enemy, y_enemy)

        enemy = None
        if coords_valid_flag:
            attacker = self.board.get_unit(x_attacker, y_attacker)
            enemy = self.board.get_unit(x_enemy, y_enemy)
        else:
            return False

        if enemy is None or attacker is None:
            return False

        if not attacker.fraction == fraction:
            return False

        if hasattr(attacker, 'attack'):
            attacker.attack(enemy)
        else:
            return False

        if isinstance(enemy, MotherBaseUnit):
            attack_decorator = AttackedDecorator()
            enemy = attack_decorator(enemy)

        self.board.set_unit(x_enemy, y_enemy, enemy)
        return True


class CreatingCommand (Command):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self, args: list, fraction: 'str', fabrics: dict) -> bool:
        x = int(args[0])
        y = int(args[1])
        description = args[2]
        
        unit = None
        cost = None
        common_descriptions = ['flyer', 'division']
        
        if not self.board.valid_coords(x, y):
            return False

        # Создание unit'ов только на "своей" половине карты
        if fraction == Fractions().Fremen() and (x + y + 1) >= self.board.side_length:
            return False
        elif fraction == Fractions().Harkonnen() and (x + y + 1) <= self.board.side_length:
            return False

        if description == 'harvester' and fraction == Fractions().Harkonnen():
            unit = fabrics['motherbase_harkonnen'].create_motherbase(x, y)
        elif description == 'village' and fraction == Fractions().Fremen():
            unit = fabrics['motherbase_fremen'].create_motherbase(x, y)
        elif description in common_descriptions:
            fabric = None

            if fraction == Fractions().Fremen():
                fabric = fabrics['war_fremen']
            else:
                fabric = fabrics['war_harkonnen']

            if description == 'flyer':
                unit = fabric.create_flyer(x, y)
            elif description == 'division':
                unit = fabric.create_division(x, y)
        else:
            return False

        cost = unit.get_cost()
        if fraction == Fractions().Fremen() and cost > self.board.get_fremen_melange():
            return False
        elif fraction == Fractions().Harkonnen() and cost > self.board.get_harkonnen_melange():
            return False

        if fraction == Fractions().Fremen():
            self.board.change_fremen_melange(-cost)
        elif fraction == Fractions().Harkonnen():
            self.board.change_harkonnen_melange(-cost)

        self.board.set_unit(x, y, unit)
        return True


class EmptyCommand (Command):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self) -> bool:
        return True