__ver__ = "0.3.1"
import math

def engine(radius):
    return {
        "radius": radius,
        "diameter": radius * 2,
        "circumference": 2 * math.pi * radius,
        "area": math.pi * radius ** 2
    }

def normalize(key, val):
    if key == "r":
        return val
    elif key == "d":
        return val / 2
    elif key == "c":
        return val / (2 * math.pi)
    elif key == "a":
        return math.sqrt(val / math.pi)
    else:
        return None

def solve(key, val):
    return engine(normalize(key, val))