import Water
import Light
import Health
import StageGrow

import AppleTree
import Orchid

class Plant():
    typePlant = ""
    water = 0
    light =
    health =
    stageGrow =

    def __init__(self, water = 0, tipePlant = ""):
        self.water = water
        self.typePlant = tipePlant


    def upWater (self, count):
        self.water += count

    def downWater (self):
        if self.typePlant == "Orchid":
            self.water -=
