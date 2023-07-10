from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Aspect:
    fst_planet: ClassVar[dict[str, str, bool, int]] = {}
    snd_planet: ClassVar[dict[str, str, bool, int]] = {}
    name: str
    degree: str

@dataclass
class Planet:
    name: str
    degree: str
    is_retrograde: bool = False
    house: int = None
    t_dependency: int = 0 # 0 - не зависит, например

class NatalChart(Planet):
    def __init__(self, placements):
        self.sun = Planet(placements[0][0], placements[0][1], placements[0][2], True)
        """self.moon = Planet(placements[1][0], placements[1][1], placements[1][2], True)
        self.mercury = Planet(placements[2][0], placements[2][1], placements[2][2], True)
        self.venus = Planet(placements[3][0], placements[3][1], placements[3][2], True)
        self.mars = Planet(placements[4][0], placements[4][1], placements[4][2], True)
        self.jupiter = Planet(placements[5][0], placements[5][1], placements[5][2], True)
        self.saturn = Planet(placements[6][0], placements[6][1], placements[6][2], True)
        self.neptune = Planet(placements[7][0], placements[7][1], placements[7][2], True)
        self.uranus = Planet(placements[8][0], placements[8][1], placements[8][2], True)
        self.pluto = Planet(placements[9][0], placements[9][1], placements[9][2], True)
        self.chiron = Planet(placements[10][0], placements[10][1], placements[10][2], True)
        self.lilith = Planet(placements[11][0], placements[11][1], placements[11][2], True)
        self.selena = Planet(placements[12][0], placements[12][1], placements[12][2], True)
        self.north_node = Planet(placements[13][0], placements[13][1], placements[13][2], True)
        self.path_of_fortune = Planet(placements[14][0], placements[14][1], placements[14][2], True)"""


print(NatalChart)
