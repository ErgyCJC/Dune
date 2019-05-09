from units import *


def test_fractions():
    test_frac = Fractions()

    assert(test_frac.Harkonnen() == 'HouseHarkonnen') is True
    assert(test_frac.Fremen() == 'Fremen') is True


def test_unit():
    test_unit = Unit()
    x, y = 18, -65

    test_unit.set_coords(x, y)
    assert(test_unit.x == x and test_unit.y == y) is True
    assert(test_unit.get_x() == x) is True
    assert(test_unit.get_y() == y) is True
    assert(test_unit.get_coords() == [x, y]) is True

    x, y = 34, 5
    test_unit.set_x(x)
    assert(test_unit.get_x() == x) is True
    test_unit.set_y(y)
    assert(test_unit.get_y() == y) is True
    
    test_unit.set_fraction(Fractions().Fremen())
    assert(test_unit.fraction == Fractions().Fremen()) is True
    test_unit.set_fraction(Fractions().Harkonnen())
    assert(test_unit.fraction == Fractions().Harkonnen()) is True

    assert(test_unit.is_alive()) is True


def test_warunit():
    x, y = 56, 32
    test_warunit = WarUnit(x, y)
    assert(test_warunit.get_coords() == [x, y]) is True

    value = 45
    test_warunit.set_damage(value)
    assert(test_warunit.damage == value) is True

    value = 76
    test_warunit.set_health(value)
    assert(test_warunit.health == value) is True
    assert(test_warunit.is_alive()) is True
    value = -13
    test_warunit.set_health(value)
    assert(test_warunit.is_alive()) is False
    delta = 54
    test_warunit.change_health(delta)
    assert(test_warunit.health == value + delta) is True

    value = 91
    enemy_warunit = WarUnit(x, y)
    enemy_warunit.set_health(value)
    
    test_warunit.attack(enemy_warunit)
    assert(enemy_warunit.health == value - test_warunit.damage) is True


def test_movingwarunit():
    x, y = 13, 15
    test_unit = MovingWarUnit(x, y)
    
    delta_x, delta_y = -4, 7
    test_unit.change_coords(delta_x, delta_y)
    assert(test_unit.get_coords() == [x + delta_x, y + delta_y])

    x += delta_x
    y += delta_y
    test_unit.change_x(delta_x)
    test_unit.change_y(delta_y)
    assert(test_unit.get_coords() == [x + delta_x, y + delta_y])

    value = 78
    test_unit.set_speed(value)
    assert(test_unit.speed == value) is True


def test_motherbaseunit():
    x, y = 9, 8
    test_unit = MotherBaseUnit(x, y)
    
    melange = 4
    test_unit.set_melange(melange)
    assert(test_unit.melange == melange) is True

    health = 86
    test_unit.set_health(health)
    assert(test_unit.health == health) is True

    assert(test_unit.is_alive()) is True
    health = -6
    test_unit.set_health(health)
    assert(test_unit.is_alive()) is False
    health = 0
    test_unit.set_health(health)
    assert(test_unit.is_alive()) is False

    health_delta = 5
    test_unit.change_health(health_delta)
    assert(test_unit.health == health + health_delta) is True


def test_div_builder():
    x, y = 5, 6
    fraction = Fractions().Fremen()
    health = 56
    damage = 9
    speed = 4

    division = DivisionBuilder().get_division(fraction, x, y, health, damage, speed)

    assert(division.get_coords() == [x, y])
    assert(division.fraction == fraction)
    assert(division.health == health)
    assert(division.damage == damage)
    assert(division.speed == speed)


def test_flyer_builder():
    x, y = 9, 13
    fraction = Fractions().Harkonnen()
    health = 32
    damage = 1
    speed = 2

    flyer = FlyerBuilder().get_flyer(fraction, x, y, health, damage, speed)

    assert(flyer.get_coords() == [x, y])
    assert(flyer.fraction == fraction)
    assert(flyer.health == health)
    assert(flyer.damage == damage)
    assert(flyer.speed == speed)


def test_base_builder():
    x, y = 54, 23
    health = 3
    melange = 80

    fraction = Fractions().Fremen()
    base = MotherBaseBuider().get_unit(fraction, x, y, health, melange)

    assert(type(base) == type(Village(0, 0))) is True
    assert(base.fraction == fraction) is True
    assert(base.get_coords() == [x, y]) is True
    assert(base.health == health) is True
    assert(base.melange == melange) is True

    fraction = Fractions().Harkonnen()
    base = MotherBaseBuider().get_unit(fraction, x, y, health, melange)

    assert(type(base) == type(Harvester(0, 0))) is True
    assert(base.fraction == fraction) is True
    assert(base.get_coords() == [x, y]) is True
    assert(base.health == health) is True
    assert(base.melange == melange) is True


def test_war_fabric():
    x, y = 45, 21
    
    fraction = Fractions().Fremen()
    division = WarUnitsFabric(fraction).create_division(x, y)
    assert(division.fraction == fraction) is True
    assert(division.get_coords() == [x, y]) is True
    assert(division.speed == 2) is True
    assert(division.damage == 35) is True
    assert(division.health == 75) is True

    fraction = Fractions().Harkonnen()
    division = WarUnitsFabric(fraction).create_division(x, y)
    assert(division.fraction == fraction) is True
    assert(division.get_coords() == [x, y]) is True
    assert(division.speed == 2) is True
    assert(division.damage == 25) is True
    assert(division.health == 50) is True

    fraction = Fractions().Fremen()
    flyer = WarUnitsFabric(fraction).create_flyer(x, y)
    assert(flyer.fraction == fraction) is True
    assert(flyer.get_coords() == [x, y]) is True
    assert(flyer.speed == 4) is True
    assert(flyer.damage == 15) is True
    assert(flyer.health == 25) is True

    fraction = Fractions().Harkonnen()
    flyer = WarUnitsFabric(fraction).create_flyer(x, y)
    assert(flyer.fraction == fraction) is True
    assert(flyer.get_coords() == [x, y]) is True
    assert(flyer.speed == 4) is True
    assert(flyer.damage == 15) is True
    assert(flyer.health == 25) is True


def test_base_fabric():
    x, y = 67, -2

    fraction = Fractions().Fremen()
    base = MotherBaseFabric(fraction).create_motherbase(x, y)
    assert(type(base) == type(Village(0, 0)))
    assert(base.get_coords() == [x, y])
    assert(base.melange == 4)
    assert(base.health == 400)

    fraction = Fractions().Harkonnen()
    base = MotherBaseFabric(fraction).create_motherbase(x, y)
    assert(type(base) == type(Harvester(0, 0)))
    assert(base.get_coords() == [x, y])
    assert(base.melange == 9)
    assert(base.health == 250)