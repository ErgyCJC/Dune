from board import *


class DuneGame:

    def __init__(self, board_size: int):
        self.board = Board(board_size)
        
        """
        Singleton
        Разрешён только один экземпляр класса игры,
        'конструктор' принудительно удаляется после.
        """
        self.__init__ = None

    def mainloop(self):
        pass