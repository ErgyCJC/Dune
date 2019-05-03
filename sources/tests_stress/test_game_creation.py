from dune import *


def test_create_incorrect_game():
    incorrect_size = 1
    test_game = DuneGame(incorrect_size)

    min_size = 2

    assert((test_game.board.side_length >= min_size) is True)


def test_create_large_incorrect_game():
    incorrect_size = -500
    test_game = DuneGame(incorrect_size)

    min_size = 2

    assert((test_game.board.side_length >= min_size) is True)