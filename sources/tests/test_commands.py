from board import *
from command import *
from units import *


def test_empty_command():
    test_board = Board()
    command = EmptyCommand(test_board)

    assert(command())


def test_attack():
    test_board = Board()
    command = AttackCommand(test_board)

    args1 = ['-45', '-45', '45', '6']
    fremen_fraction = Fractions().Fremen()
    assert(command(args1, fremen_fraction) is False)

    args2 = ['0', '0', '1', '0']
    assert(command(args2, fremen_fraction) is False)

    flyer = Flyer(0, 0)
    flyer.set_fraction = Fractions().Harkonnen()
    test_board.set_unit(0, 0, flyer)
    assert(command(args2, fremen_fraction) is False)

    flyer = Flyer(0, 0)
    flyer.set_fraction(fremen_fraction)
    flyer.set_health(5)
    flyer.set_damage(5)
    test_board.set_unit(0, 0, flyer, True)
    base = Harvester(1, 0)
    base.set_health(15)
    test_board.set_unit(1, 0, base)
    assert(command(args2, fremen_fraction) is True)


def test_move():
    test_board = Board()
    command = MoveCommand(test_board)
    fremen_fraction = Fractions().Fremen()

    flyer = Flyer(0, 0)
    flyer.set_fraction(fremen_fraction)
    flyer.set_speed(2)

    incorrect_args = ['-656', '0', '3', '-3']
    assert(command(incorrect_args, fremen_fraction) is False)

    correct_args = ['0', '0', '1', '1']

    flyer.set_speed(-56)
    test_board.set_unit(0, 0, flyer, True)
    assert(command(correct_args, fremen_fraction) is False)

    flyer.set_fraction = Fractions().Harkonnen()
    test_board.set_unit(0, 0, flyer, True)
    assert(command(correct_args, fremen_fraction) is False)

    long_distance_args = ['0', '0', '7', '9']
    flyer.set_speed(2)
    flyer.set_fraction = fremen_fraction
    test_board.set_unit(0, 0, flyer, True)
    assert(command(long_distance_args, fremen_fraction) is False)

    assert(command(correct_args, fremen_fraction) is True)


def test_create():
    test_board = Board()
    command = CreatingCommand(test_board)
    fremen_fraction = Fractions().Fremen()
    harkonnen_fraction = Fractions().Harkonnen()
    incorrect_fraction = 'fjnvjfnv'

    war_fabric_fremen = WarUnitsFabric(Fractions().Fremen())
    war_fabric_harkonnen = WarUnitsFabric(Fractions().Harkonnen())
    motherbase_fabric_fremen = MotherBaseFabric(Fractions().Fremen())
    motherbase_fabric_harkonnen = MotherBaseFabric(Fractions().Harkonnen())

    fabrics_set = {'war_fremen' : war_fabric_fremen,
                    'war_harkonnen' : war_fabric_harkonnen,
                    'motherbase_fremen' : motherbase_fabric_fremen,
                    'motherbase_harkonnen' : motherbase_fabric_harkonnen}

    args = ['0', '0', 'division']
    assert(command(args, incorrect_fraction, fabrics_set) is False)

    incorrect_args = ['-1', '1000', 'flyer']
    assert(command(incorrect_args, fremen_fraction, fabrics_set) is False)

    incorrect_args = ['0', '0', 'incorrect_name']
    assert(command(incorrect_args, fremen_fraction, fabrics_set) is False)

    incorrect_args = ['15', '15', 'incorrect_name']
    assert(command(incorrect_args, fremen_fraction, fabrics_set) is False)

    test_board.change_fremen_melange(-100)
    test_board.change_harkonnen_melange(-100)
    assert(command(args, fremen_fraction, fabrics_set) is False)

    test_board.change_fremen_melange(200)
    test_board.change_harkonnen_melange(200)
    assert(command(['0', '0', 'division'], fremen_fraction, fabrics_set) is True)
    assert(command(['0', '0', 'flyer'], fremen_fraction, fabrics_set) is True)
    assert(command(['0', '0', 'village'], fremen_fraction, fabrics_set) is True)
    
    assert(command(['13', '13', 'division'], harkonnen_fraction, fabrics_set) is True)
    assert(command(['9', '13', 'flyer'], harkonnen_fraction, fabrics_set) is True)
    assert(command(['9', '9', 'harvester'], harkonnen_fraction, fabrics_set) is True)
