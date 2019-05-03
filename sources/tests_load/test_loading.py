from dune import *


def test_many_units_16():
    board_size = 16
    game = DuneGame(board_size)

    for x in range(board_size):
        for y in range(board_size):
            if not (x is 0 and y is 0) and not (x is board_size - 1 and y is board_size - 1):
                assert(game.create_fremen_motherbase(x, y) is True)

    for x in range(board_size):
        for y in range(board_size):
                assert(game.create_harkonnen_motherbase(x, y) is False)


def test_many_units_64():
    board_size = 64
    game = DuneGame(board_size)

    for x in range(board_size):
        for y in range(board_size):
            if not (x is 0 and y is 0) and not (x is board_size - 1 and y is board_size - 1):
                assert(game.create_fremen_motherbase(x, y) is True)

    for x in range(board_size):
        for y in range(board_size):
                assert(game.create_harkonnen_motherbase(x, y) is False)


def test_many_units_128():
    board_size = 128
    game = DuneGame(board_size)

    for x in range(board_size):
        for y in range(board_size):
            if not (x is 0 and y is 0) and not (x is board_size - 1 and y is board_size - 1):
                assert(game.create_fremen_motherbase(x, y) is True)

    for x in range(board_size):
        for y in range(board_size):
                assert(game.create_harkonnen_motherbase(x, y) is False)