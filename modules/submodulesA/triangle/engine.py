__ver__ = "0.2.0"
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

def normalize(key, val1, val2, val3):
    if key == "b":
        return val1, val2
    elif key == "h":
        return pythagoras("a", val1, val2), val2
    elif key == "p" and val3 is not None:
        val1 -= (val2 + val3)
        hypotenuse = max(val1, val2, val3)
        base = (val1 + val2 + val3) - max(val1, val2, val3) - min(val1, val2, val3)
        height = min(val1, val2, val3)
        return base, height
    elif key == "a":
        return (2 * val1) / val2, val2
    else:
        return None, None

def solve(key, val1, val2, val3=None):
    base, height = normalize(key, val1, val2, val3)
    return engine(base, height)