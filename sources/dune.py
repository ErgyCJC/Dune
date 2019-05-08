from board import *
from units import *
from drawer import *
from command import *
from strategies import *


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

        self.turn_number = 0
        self.drawer = Drawer(self.board)
        self.__init__ = None

    def create_fremen_motherbase(self, x: int, y: int) -> bool:
        return self.board.set_unit(x, y, self.motherbase_fabric_fremen.create_motherbase(x, y))

    def create_harkonnen_motherbase(self, x: int, y: int) -> bool:
        return self.board.set_unit(x, y, self.motherbase_fabric_harkonnen.create_motherbase(x, y))

    def mainloop(self):
        self.end_game_flag = False
        self.turn_number = 0

        while not self.end_game_flag:
            self.drawer.draw(self.turn_number, self.board.get_fremen_melange())
            
            turn_result = self.player_turn()
            if self.end_game_flag or not turn_result:
                continue
            
            self.update_game_state()

            turn_result = self.robot_turn()
            if self.end_game_flag or not turn_result:
                continue

            self.update_game_state()

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
        elif command_args[0] == 'pass':
            command = EmptyCommand(self.board)
            command_result = command()
        elif command_args[0] == 'exit':
            self.end_game_flag = True

        return command_result

    def robot_turn(self) -> bool:
        turn_producer = RobotStrategy()
        turn_args = turn_producer.produce_turn(self.board, UnitsInfo.units_costs)

        command_result = None
        if turn_args[0] == 'empty':
            command_result = turn_args[1]()
        elif turn_args[0] == 'create':
            command_result = turn_args[1](turn_args[2:], Fractions().Harkonnen(), self.fabrics_set)
        elif turn_args[0] == 'attack':
            command_result = turn_args[1](turn_args[2], Fractions().Harkonnen())

    def check_win(self) -> None:
        if self.board.get_unit(0, 0) is None:
            self.end_game_flag = True
            print('Harkonnen win!')
        elif self.board.get_unit(self.board.side_length - 1, self.board.side_length - 1) is None:
            self.end_game_flag = True
            print('Fremen win!')

    def update_board(self):
        self.board.update_board()

    def update_game_state(self):
        self.update_board()
        self.board.earn_melange()
        self.check_win()
        self.turn_number += 1