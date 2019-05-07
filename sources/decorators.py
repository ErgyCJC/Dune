from units import *


class AttackedDecorator:
    def __init__(self):
        pass

    def __call__(self, unit: MotherBaseUnit):
        unit.previous_melange = unit.melange
        unit.melange = 0
        return unit


class ReconstructedDecorator:
    def __init__(self):
        pass
    
    def __call__(self, unit: MotherBaseUnit):
        unit.melange = unit.previous_melange
        return unit