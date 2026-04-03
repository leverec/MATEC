__ver__ = "0.1.0"
import math

PI: float = math.pi

class BaseCircle:
    def result(self):
        return {
            "radius": self.radius,
            "diameter": self.diameter,
            "circumference": self.circumference,
            "area": self.area
        }

class Circle_by_radius(BaseCircle):
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius
        self.circumference = 2 * PI * radius
        self.area = PI * radius ** 2

class Circle_by_diameter(BaseCircle):
    def __init__(self, diameter):
        self.radius = diameter / 2
        self.diameter = diameter
        self.circumference = PI * diameter
        self.area = PI * self.radius ** 2

class Circle_by_circumference(BaseCircle):
    def __init__(self, circumference):
        self.radius = (circumference / PI)/ 2
        self.diameter = circumference / PI
        self.circumference = circumference
        self.area = PI * self.radius ** 2

class Circle_by_area(BaseCircle):
    def __init__(self, area):
        self.radius = math.sqrt(area / PI)
        self.diameter = self.radius * 2
        self.circumference = PI * self.diameter
        self.area = area