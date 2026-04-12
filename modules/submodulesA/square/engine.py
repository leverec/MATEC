__ver__ = "0.3.1"
import math

def engine(side):
    return {
        "side": side,
        "diagonal": side * math.sqrt(2),
        "perimeter": 4 * side,
        "area": side ** 2
    }

def normalize(key, val):
    if key == "s":
        return val
    elif key == "d":
        return val / math.sqrt(2)
    elif key == "p":
        return val / 4
    elif key == "a":
        return math.sqrt(val)
    else:
        return None

def solve(key, val):
    return engine(normalize(key, val))