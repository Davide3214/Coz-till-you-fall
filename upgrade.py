from button import Button
from growthPoints import GrowthPoints

class Upgrade:
    def __init__(self):
        self.__rootAug = 30
        self.__multAug = 26
        self.__ppsAug = 25

    def upgRoot(self, button: Button, growPoint: GrowthPoints):
        growPoint.spend(button.getUpgCost())
        button.setUpgCost(self.__rootAug)

    def upgMult(self, button: Button, growPoint: GrowthPoints):
        growPoint.spend(button.getUpgCost())
        growPoint.setMultiplier()
        button.setUpgCost(self.__multAug)

    def upgPPS(self, button: Button, growPoint: GrowthPoints):
        growPoint.spend(button.getUpgCost())
        growPoint.setAddPoints()
        button.setUpgCost(self.__ppsAug)
