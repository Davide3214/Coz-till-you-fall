class Camera:
    def __init__(self):
        self.__y = 0

    def moveUp(self):
        if self.__y > -1400:
            self.__y -= 1

    def moveDown(self):
        if self.__y < 0:
            self.__y += 1

    def getY(self):
        return self.__y