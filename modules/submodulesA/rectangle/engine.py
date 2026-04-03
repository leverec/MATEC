__ver__ = "0.1.0"
import math

class BaseRectangle:
    def result(self):
        return {
            "length": self.length,
            "width": self.width,
            "diagonal": self.diagonal,
            "perimeter": self.perimeter,
            "area": self.area
        }

class Rectangle_by_base(BaseRectangle):
    def __init__(self, length, width):
        self.length = max(length, width)
        self.width = min(length, width)
        self.diagonal = math.sqrt(pow(length, 2) + pow(width, 2))
        self.perimeter = 2 * (length + width)
        self.area = length * width

class Rectangle_by_diagonal(BaseRectangle):
    def __init__(self, diagonal, side_a):
        self.side_b = math.sqrt(pow(diagonal, 2) - pow(side_a, 2))
        self.length = max(side_a, self.side_b)
        self.width = min(side_a, self.side_b)
        self.diagonal = diagonal
        self.perimeter = 2 * (self.length + self.width)
        self.area = self.length * self.width

class Rectangle_by_perimeter(BaseRectangle):
    def __init__(self, perimeter, side_a):
        self.side_b = perimeter / 2 - side_a
        self.length = max(side_a, self.side_b)
        self.width = min(side_a, self.side_b)
        self.diagonal = math.sqrt(pow(self.length, 2) + pow(self.width, 2))
        self.perimeter = perimeter
        self.area = self.length * self.width

class Rectangle_by_area(BaseRectangle):
    def __init__(self, area, side_a):
        self.side_b = area / side_a
        self.length = max(side_a, self.side_b)
        self.width = min(side_a, self.side_b)
        self.diagonal = math.sqrt(pow(self.length, 2) + pow(self.width, 2))
        self.perimeter = 2 * (self.length + self.width)
        self.area = area