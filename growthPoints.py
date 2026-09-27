class GrowthPoints:
    def __init__(self):
        self.__points = 0.0
        self.__addPoints = 1
        self.__multiplier = 1.0

    def add(self):
        self.__points += self.__addPoints*self.__multiplier

    def getPoints(self):
        return self.__points

    def setAddPoints(self):
        self.__addPoints += 1

    def setMultiplier(self):
        self.__multiplier += 0.2

    def spend(self, points):
        self.__points -= points