__ver__ = "0.1.0"
import math

class BaseSquare:
    def result(self):
        return {
            "side": self.side,
            "diagonal": self.diagonal,
            "perimeter": self.perimeter,
            "area": self.area
        }

class Square_by_side(BaseSquare):
    def __init__(self, side):
        self.side = side
        self.diagonal = side * math.sqrt(2)
        self.perimeter = side * 4
        self.area = side ** 2

class Square_by_diagonal(BaseSquare):
    def __init__(self, diagonal):
        self.side = diagonal * math.sqrt(2) / 2
        self.diagonal = diagonal
        self.perimeter = self.side * 4
        self.area = self.side ** 2

class Square_by_perimeter(BaseSquare):
    def __init__(self, perimeter):
        self.side = perimeter / 4
        self.diagonal = self.side * math.sqrt(2)
        self.perimeter = perimeter
        self.area = self.side ** 2

class Square_by_area(BaseSquare):
    def __init__(self, area):
        self.side = math.sqrt(area)
        self.diagonal = self.side * math.sqrt(2)
        self.perimeter = self.side * 4
        self.area = area