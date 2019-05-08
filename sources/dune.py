from board import *
from units import *
from drawer import *
from command import *
from robot_strategy import *


class DuneGame:

    def __init__(self, board_size: int):
        if board_size < 2:
            board_size = 2

        self.board = Board(board_size)
        
        self.war_fabric_fremen = WarUnitsFabric(Fractions().Fremen())
        self.war_fabric_harkonnen = WarUnitsFabric(Fractions().Harkonnen())
        self.motherbase_fabric_fremen = MotherBaseFabric(Fractions().Fremen())
        self.motherbase_fabric_harkonnen = MotherBaseFabric(Fractions().Harkonnen())

        self.fabrics_set = {'war_fremen' : self.war_fabric_fremen,
                            'war_harkonnen' : self.war_fabric_harkonnen,
                            'motherbase_fremen' : self.motherbase_fabric_fremen,
                            'motherbase_harkonnen' : self.motherbase_fabric_harkonnen}

        self.start_village = self.motherbase_fabric_fremen.create_motherbase(0, 0)
        self.board.set_unit(0, 0, self.start_village)
        
        limit_coord = board_size - 1
        self.start_harvester = self.motherbase_fabric_harkonnen.create_motherbase(limit_coord, limit_coord)
        self.board.set_unit(limit_coord, limit_coord, self.start_harvester)

        self.units_count = 2
        self.max_units_count = board_size * board_size

        self.drawer = Drawer(self.board)

        """
        Singleton
        Разрешён только один экземпляр класса игры,
        'конструктор' принудительно удаляется после создания первого объекта.
        """
        self.__init__ = None

    def create_fremen_motherbase(self, x: int, y: int) -> bool:
        return self.board.set_unit(x, y, self.motherbase_fabric_fremen.create_motherbase(x, y))

    def create_harkonnen_motherbase(self, x: int, y: int) -> bool:
        return self.board.set_unit(x, y, self.motherbase_fabric_harkonnen.create_motherbase(x, y))

    def mainloop(self):
        self.end_game_flag = False
        current_fraction = Fractions().Fremen()
        turn_number = 0

        while not self.end_game_flag:
            self.drawer.draw(turn_number)
            
            turn_result = self.player_turn()
            if self.end_game_flag or not turn_result:
                continue
            
            self.update_board()
            self.check_win()
            turn_number += 2

    def player_turn(self) -> bool:
        print('>>> ', end='')

        command_args = input().split()
        command_result = False
        
        if command_args == []:
            return False
        elif command_args[0] == 'move':
            command = MoveCommand(self.board)
            command_result = command(command_args[1:], Fractions().Fremen())
        elif command_args[0] == 'attack':
            command = AttackCommand(self.board)
            command_result = command(command_args[1:], Fractions().Fremen())
        elif command_args[0] == 'create':
            command = CreatingCommand(self.board)
            command_result = command(command_args[1:], Fractions().Fremen(), self.fabrics_set)
        elif command_args[0] == 'exit':
            self.end_game_flag = True

        return command_result

    def robot_turn(self):
        pass

    def check_win(self) -> None:
        if self.board.get_unit(0, 0) is None:
            self.end_game_flag = True
            print('Harkonnen win!')
        elif self.board.get_unit(self.board.side_length - 1, self.board.side_length - 1) is None:
            self.end_game_flag = True
            print('Fremen win!')

    # Очистка от unit'ов с отрицательным здоровьем
    def update_board(self):
        for x in range(self.board.side_length):
            for y in range(self.board.side_length):
                
                unit = self.board.get_unit(x, y)
                if unit is not None:
                    if hasattr(unit, 'health') and unit.health <= 0:
                        self.board.set_unit(x, y, None, True)
