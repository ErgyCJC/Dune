import board
from units import *


class TestUnitClass:
        def __init__(self):
            pass

""" TESTS """

def test_size():
    size = 16
    test_board = board.Board(size)

    assert(test_board.side_length == size) is True


def test_matrix():
    size = 16
    test_board = board.Board(size)

    assert(len(test_board.board) == size) is True
    for x in test_board.board:
        assert(len(x) == size) is True


def test_get_size():
    size = 16
    test_board = board.Board(size)

    assert(test_board.get_size() == size) is True


def test_set_unit():
    size = 16
    x = y = size // 2
    test_board = board.Board(size)

    test_unit = TestUnitClass()
    test_board.set_unit(x, y, test_unit)

    assert(type(test_unit) == type(test_board.board[x][y])) is True
    assert(test_unit is test_board.board[x][y]) is True


def test_is_unit_true():
    size = 16
    test_board = board.Board(size)

    assert(test_board.is_unit(0, 0) is False)


def test_is_unit_true():
    size = 16
    test_board = board.Board(size)
    test_board.set_unit(0, 0, TestUnitClass())

    assert(test_board.is_unit(0, 0) is True)


def test_valid_coords():
    size = 16
    test_board = board.Board(size)

    assert(test_board.valid_coords(4, 5) is True)
    assert(test_board.valid_coords(0, 0) is True)
    assert(test_board.valid_coords(size - 1, size - 1) is True)
    
    assert(test_board.valid_coords(-3, 4) is False)
    assert(test_board.valid_coords(6, - 3) is False)
    assert(test_board.valid_coords(6, size + 3) is False)
    assert(test_board.valid_coords(size + 3, 4) is False)


def test_get_unit():
    size = 16
    x = y = size // 2
    test_board = board.Board(size)
    test_unit = TestUnitClass()
    test_board.set_unit(x, y, test_unit)

    assert(test_board.get_unit(x, y) is test_unit)


def test_remove_unit():
    size = 16
    x = y = size // 2
    test_board = board.Board(size)
    test_unit = TestUnitClass()
    test_board.set_unit(x, y, test_unit)
    
    assert(test_board.get_unit(x, y) is test_unit) is True
    test_board.remove_unit(x, y)
    assert(test_board.get_unit(x, y) is None) is True


def test_is_full():
    test_board = board.Board()

    assert(test_board.is_full() is False) is True

    unit = Flyer(0, 0)
    test_board.set_unit(0, 0, unit)

    assert(test_board.is_full() is False) is True


def test_recalc_filled():
    test_board = board.Board()

    assert(test_board.recalc_filled_count() == 0) is True

    unit = Flyer(0, 0)
    test_board.set_unit(0, 0, unit)

    assert(test_board.recalc_filled_count() == 1) is True

    test_board.set_unit(0, 1, unit)
    test_board.set_unit(1, 0, unit)
    test_board.set_unit(1, 1, unit)

    assert(test_board.recalc_filled_count() == 4) is True


def test_get_fremen_melange():
    test_board = board.Board()
    
    assert(test_board.get_fremen_melange() == 10) is True


def test_get_harkonnen_melange():
    test_board = board.Board()
    
    assert(test_board.get_harkonnen_melange() == 10) is True


def test_change_fremen_melange():
    test_board = board.Board()
    test_board.change_fremen_melange(5)
    
    assert(test_board.get_fremen_melange() == 15) is True


def test_change_harkonnen_melange():
    test_board = board.Board()
    test_board.change_harkonnen_melange(5)
    
    assert(test_board.get_harkonnen_melange() == 15) is True


def test_earn_melange():
    test_board = board.Board()
    village = Village(0, 0)
    village.set_melange(1)
    test_board.set_unit(0, 0, village)

    assert(test_board.get_fremen_melange() == 10) is True

    test_board.earn_melange()

    assert(test_board.get_fremen_melange() == 11) is True


def test_update():
    test_board = board.Board()
    unit = Flyer(0, 0)
    unit.set_health(-45)
    test_board.update_board()
    
    assert(test_board.get_unit(0, 0) is None) is True