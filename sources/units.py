class Fractions:
    
    def __init__(self):
        self.fractions = ['HouseHarkonnen', 'Fremen']

    def __str__(self):
        return 'FractionsClass'

    def get_all(self):
        return self.fractions

    def Harkonnen(self):
        return self.fractions[0]

    def Fremen(self):
        return self.fractions[1]

    def add_fraction(self, new_fraction: str):
        if not set(self.fractions).isdisjoint(set(new_fraction)):
            self.fractions.append(new_fraction)

class UnitsInfo:
    units_costs = {'war_unit' : 9, 'motherbase' : 12}

# Units Hierarchy
class Unit:

    def __init__(self):
        self.fraction = None
        self.x = None
        self.y = None

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y

    def set_coords(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_coords(self):
        return [self.x, self.y]

    def get_y(self):
        return self.y

    def get_x(self):
        return self.x

    def __str__(self):
        return 'Unit'

    def set_fraction(self, fraction: str):
        self.fraction = fraction

    def is_alive(self):
        """
        При расширении функционала возможны Unit'ы,
        которые не возможно уничтожить (g.e. город)
        """

        return True


class WarUnit (Unit):

    def __init__(self, x: int, y: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_coords(x, y)
        self.cost = UnitsInfo.units_costs['war_unit']
        self.damage = None
        self.health = None

    def __str__(self):
        return 'WarUnit'

    def get_cost(self):
        return self.cost

    def set_damage(self, damage: int):
        self.damage = damage

    def get_attack_power(self):
        return self.damage

    def set_health(self, health: int):
        self.health = health

    def get_health(self):
        return self.health

    def attack(self, enemy: Unit):
        if enemy.is_alive() and hasattr(enemy, 'change_health'):
            enemy.change_health(-1 * self.damage)

    def is_alive(self):
        return self.health > 0

    def change_health(self, health_delta: int):
        self.health += health_delta


class MovingWarUnit (WarUnit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = None

    def change_x(self, x_delta: int):
        self.x += x_delta

    def change_y(self, y_delta: int):
        self.y += y_delta

    def change_coords(self, x_delta: int, y_delta: int):
        self.x += x_delta
        self.y += y_delta

    def set_speed(self, speed:int):
        self.speed = speed

    def __str__(self):
        return 'MovingWarUnit'


class Division (MovingWarUnit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return 'Division'


class Flyer (MovingWarUnit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return 'Flyer'


class MotherBaseUnit (Unit):
    
    def __init__(self, x: int, y: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = None
        self.melange = None
        self.set_coords(x, y)
        self.cost = UnitsInfo.units_costs['motherbase']

        # MotherBaseUnit не может быть перемещён
        self.change_x = None
        self.change_y = None
        self.set_coords = None
        self.change_coords = None

    def set_melange(self, melange: int):
        self.melange = melange

    def get_cost(self):
        return self.cost

    def set_health(self, health: int):
        self.health = health

    def get_melange(self):
        return self.melange

    def get_health(self):
        return get_health

    def change_health(self, health_delta: int):
        self.health += health_delta

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return 'MotherBaseUnit'


class Harverster (MotherBaseUnit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_fraction = None
        self.fraction = Fractions().Harkonnen()

    def __str__(self):
        return 'Harvester'


class Village (MotherBaseUnit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_fraction = None
        self.fraction = Fractions().Fremen()

    def __str__(self):
        return 'Village'


# Units Creating

class DivisionBuilder:

    def __init__(self):
        pass

    def get_division(self, fraction: str, x: int, y: int, health: int, damage: int, speed: int):
        division = Division(x, y)
        division.set_fraction(fraction)
        division.set_health(health)
        division.set_damage(damage)
        division.set_speed(speed)

        return division


class FlyerBuilder:
    
    def __init__(self):
        pass

    def get_flyer(self, fraction: str, x: int, y: int, health: int, damage: int, speed: int):
        flyer = Flyer(x, y)
        flyer.set_fraction(fraction)
        flyer.set_health(health)
        flyer.set_damage(damage)
        flyer.set_speed(speed)

        return flyer


class WarUnitsFabric:

    def __init__(self, fraction: str):
        self.fraction = fraction

    def create_division(self, x: int, y: int):
        if self.fraction == Fractions().Harkonnen():
            health = 50
            damage = 25
            speed = 1
        elif self.fraction == Fractions().Fremen():
            health = 75
            damage = 35
            speed = 1

        return DivisionBuilder().get_division(self.fraction, x, y, health, damage, speed)

    def create_flyer(self, x: int, y: int):
        health = 25
        damage = 15
        speed = 2

        return FlyerBuilder().get_flyer(self.fraction, x, y, health, damage, speed)


class MotherBaseBuider:

    def __init__(self):
        pass

    def get_unit(self, fraction: str, x: int, y: int, health: int, melange: int):
        if fraction == Fractions().Harkonnen():
            unit = Harverster(x, y)
        elif fraction == Fractions().Fremen():
            unit = Village(x, y)

        unit.set_health(health)
        unit.set_melange(melange)
        return unit


class MotherBaseFabric:

    def __init__(self, fraction: str):
        self.fraction = fraction

    def create_motherbase(self, x: int, y: int):
        if self.fraction == Fractions().Harkonnen():
            melange = 7
            health = 250
        elif self.fraction == Fractions().Fremen():
            melange = 3
            health = 500
        
        return MotherBaseBuider().get_unit(self.fraction, x, y, health, melange)
