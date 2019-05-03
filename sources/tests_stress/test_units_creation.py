from dune import *


def test_many_incorrect_units():
    incorrect_x = -50
    incorrect_y = -50

    board_size = 16
    game = DuneGame(board_size)

    for x in range(board_size):
        for y in range(board_size):
                assert(game.create_fremen_motherbase(incorrect_x - x, incorrect_y - y) is False)

    incorrect_x, incorrect_y = -incorrect_x, -incorrect_y

    for x in range(board_size):
        for y in range(board_size):
                assert(game.create_fremen_motherbase(incorrect_x + x, incorrect_y + y) is False)