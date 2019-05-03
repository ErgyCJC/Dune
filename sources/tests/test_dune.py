from dune import *


def test_init():
    size = 16
    test_game = DuneGame(size)

    assert(hasattr(test_game, 'war_fabric_fremen')) is True
    assert(hasattr(test_game, 'war_fabric_harkonnen')) is True
    assert(hasattr(test_game, 'motherbase_fabric_fremen')) is True
    assert(hasattr(test_game, 'motherbase_fabric_harkonnen')) is True

    assert(hasattr(test_game, 'start_village')) is True
    assert(hasattr(test_game, 'start_harvester')) is True


def test_create_fremen_motherbase():
    size = 16
    test_game = DuneGame(size)

    assert(test_game.create_fremen_motherbase(1, 1) is True)


def test_create_harkonnen_motherbase():
    size = 16
    test_game = DuneGame(size)

    assert(test_game.create_harkonnen_motherbase(1, 1) is True)