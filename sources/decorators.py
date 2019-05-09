from units import *


class AttackedDecorator:
    def __init__(self, turns = 3):
        self.turns = turns

    def __call__(self, unit: MotherBaseUnit):
        unit.previous_melange = unit.melange
        unit.melange = 0
        unit.reconstructing_turns = self.turns
        return unit


class ReconstructedDecorator:
    def __init__(self):
        pass
    
    def __call__(self, unit: MotherBaseUnit):
        if hasattr(unit, 'reconstructing_turns') and unit.reconstructing_turns == 0:
            unit.melange = unit.previous_melange
        return unit