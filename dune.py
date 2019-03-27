from board import *
from units import *


class DuneGame:

    def __init__(self, board_size: int):
        self.board = Board(board_size)
        
        self.war_fabric_fremen = WarUnitsFabric(Fractions().Fremen())
        self.war_fabric_harkonnen = WarUnitsFabric(Fractions().Harkonnen())
        self.motherbase_fabric_fremen = MotherBaseFabric(Fractions().Fremen())
        self.motherbase_fabric_harkonnen = MotherBaseFabric(Fractions().Harkonnen())

        self.start_village = self.motherbase_fabric_fremen.create_motherbase(0, 0)
        self.board.set_unit(0, 0, self.start_village)
        
        limit_coord = board_size - 1
        self.start_harvester = self.motherbase_fabric_harkonnen.create_motherbase(limit_coord, limit_coord)
        self.board.set_unit(limit_coord, limit_coord, self.start_harvester)

        """
        Singleton
        Разрешён только один экземпляр класса игры,
        'конструктор' принудительно удаляется после создания первого объекта.
        """
        self.__init__ = None

    def mainloop(self):
        pass
