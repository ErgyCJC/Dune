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