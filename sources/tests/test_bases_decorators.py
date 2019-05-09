from units import *
from decorators import *


def test_attacked_decorator():
    turns = 5
    decorator = AttackedDecorator(turns)
    base = Village(0, 0)

    base = decorator(base)

    assert(hasattr(base, 'previous_melange') is True)
    assert(hasattr(base, 'reconstructing_turns') is True)
    assert((base.reconstructing_turns == turns) is True)


def test_reconstructed_decorator():
    melange = 10
    turns = 5
    attacked_decorator = AttackedDecorator(turns)
    base = Village(0, 0)
    base.melange = 10

    base = attacked_decorator(base)
    base.reconstructing_turns = 0

    reconstructed_decorator = ReconstructedDecorator()
    base = reconstructed_decorator(base)

    assert(base.melange == melange)