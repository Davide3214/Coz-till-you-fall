import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


import pygame as pg

class Root:
    def __init__(self, x, y):
        self.__sprite = pg.image.load(resource_path("Sprites/root.png"))
        self.__x = x
        self.__y = y
        self.__width = 64
        self.__height = 128

    def getSprite(self):
        return self.__sprite

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getHeight(self):
        return self.__height

    def bigger(self):
        self.__height += 20
        self.__sprite = pg.transform.scale(self.__sprite, (self.__width, self.__height))