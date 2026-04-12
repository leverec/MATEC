__ver__ = "0.3.1"
import math

def pythagoras(target, a, b):
    if target == "c":
        return math.sqrt(pow(a, 2) + pow(b, 2))
    elif target in ("a", "b"):
        c = max(a, b)
        bh = min(a, b)
        return math.sqrt(pow(c, 2) - pow(bh, 2))
    else:
        return None

def engine(base, height):
    return {
        "base": max(base, height),
        "height": min(base, height),
        "hypotenuse": pythagoras("c", base, height),
        "perimeter": pythagoras("c", base, height) + base + height,
        "area": base * height / 2
    }

def normalize(key, val1, val2):
    if key == "b":
        return val1, val2
    elif key == "h":
        hypotenuse = max(val1, val2)
        side = min(val1, val2)
        return pythagoras("a", hypotenuse, side), side
    elif key == "a":
        return (2 * val1) / val2, val2
    else:
        return None, None

def solve(key, val1, val2):
    base, height = normalize(key, val1, val2)
    return engine(base, height)