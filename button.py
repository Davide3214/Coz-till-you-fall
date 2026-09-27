import pygame as pg

class Button:
    def __init__(self, background, text, x, y, upgCost):
        self.__background = background
        self.__text = text
        self.__x = x
        self.__y = y
        self.__upgCost = upgCost

    def getBackground(self):
        return self.__background

    def getText(self):
        return self.__text

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getUpgCost(self):
        return self.__upgCost

    def setUpgCost(self, augment):
        self.__upgCost += augment