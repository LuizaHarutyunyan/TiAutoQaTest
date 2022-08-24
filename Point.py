class Point:
    x = 0
    y = 0

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def __init__(self, x: object, y: object) -> object:
        self.x = x
        self.y = y