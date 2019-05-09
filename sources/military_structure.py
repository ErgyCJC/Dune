from units import *


""" Военная структура, основанная на рекурсивном использовании классов """


class WarriorsUnion:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
        self.lists = dict()

    def add_list(self, tag: str):
        self.lists[tag] = list()

    def get_list(self, tag) -> list:
        return self.lists[tag]

    def get_obj_count(self) -> int:
        return len(self.attackers) + len(self.earners)

    def add_obj(self, destination: str, obj) -> None:
        self.lists[destination].append(obj)

    def get_health(self) -> int:
        health = 0
        
        for list_obj in self.lists.values():
            for obj in list_obj:
                health += obj.get_health()

        return health

    def change_health(self, health_delta: int) -> None:
        elementary_delta = change_health / self.get_obj_count()

        health = 0
        
        for list_obj in self.lists.values():
            for index in range(len(list_obj)):
                obj = list_obj[index]

                if not obj.is_alive():
                    del list_obj[index]
                elif obj.hasattr('change_health'):
                    obj.change_health(elementary_delta)

    def get_attack_power(self) -> int:
        attack_power = 0
        
        for list_obj in self.lists.values():
            for obj in list_obj:
                attack_power += obj.get_attack_power()

        return attack_power

    def is_alive(self) -> bool:
        return self.get_health() is 0

    def attack(self, enemy) -> None:
        if enemy.is_alive() and hasattr(enemy, 'change_health'):
            enemy.change_health(-1 * self.get_attack_power())

    def __str__(self) -> str:
        return 'WarriorsUnion'


class Corps (WarriorsUnion):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.attackers_tag = 'attackers'
        self.attackers_count = 10
        self.lists[self.attackers_tag] = list()

    def add_attacker(self, attacker):
        if len(self.get_list(self.attackers_tag)) < self.attackers_count:
            self.add_obj(self.attackers_tag, attacker)


class Army (WarriorsUnion):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.attackers_tag = 'attackers'
        self.earners_tag = 'earners'
        
        self.lists[self.attackers_tag] = list()
        self.lists[self.earners_tag] = list()

        self.attackers_count = 50
        self.earners_count = 50

    def add_attacker(self, attacker):
        if len(self.get_list(self.attackers_tag)) < self.attackers_count:
            self.add_obj(self.attackers_tag, attacker)

    def add_earner(self, earner):
        if len(self.get_list(self.earners_tag)) < self.earners_count:
            self.add_obj(self.earners_tag, earner)