import board

class Unit:
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

    test_unit = Unit()
    test_board.set_unit(x, y, test_unit)

    assert(type(test_unit) == type(test_board.board[x][y])) is True
    assert(test_unit is test_board.board[x][y]) is True


def test_get_unit():
    size = 16
    x = y = size // 2
    test_board = board.Board(size)
    test_unit = Unit()
    test_board.set_unit(x, y, test_unit)

    assert(test_board.get_unit(x, y) is test_unit)


def test_remove_unit():
    size = 16
    x = y = size // 2
    test_board = board.Board(size)
    test_unit = Unit()
    test_board.set_unit(x, y, test_unit)
    
    assert(test_board.get_unit(x, y) is test_unit) is True
    test_board.remove_unit(x, y)
    assert(test_board.get_unit(x, y) is None) is True