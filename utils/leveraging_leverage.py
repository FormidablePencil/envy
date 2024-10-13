from enum import Enum, auto
from dataclasses import dataclass

# TODO Will be accessible to everyone
class WealthCreation:
    def make_money():
        raise Exception("TODO") # TODO

class LeverageCreation:
    def __init__():
        raise Exception("TODO") # TODO

class EnergyE(Enum):
    Monetary = auto()
    Leverage = auto()
    Energy = auto()

@dataclass
class CreateResponse:
    message: str
    statistics: any # TODO any for now

class Energy:
    def create(type: EnergyE) -> CreateResponse:
        # Save to database of notes
        # Respond with possible conflicts
        raise Exception("TODO") # TODO
