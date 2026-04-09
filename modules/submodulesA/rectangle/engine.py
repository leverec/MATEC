__ver__ = "0.2.1"
import math

def engine(length, width):
    return {
        "length": max(length, width),
        "width": min(length, width),
        "diagonal": math.sqrt(pow(length, 2) + pow(width, 2)),
        "perimeter": 2 * (length + width),
        "area": length * width
    }

def normalize(key, val1, val2):
    if key == "b":
        return val1, val2
    elif key == "d":
        val2 = math.sqrt(val1 - val2)
        return val1, val2
    elif key == "p":
        val1 /= 2 - val2
        return val1, val2
    elif key == "a":
        val1 /= val2
        return val1, val2
    else:
        return None, None

def solve(key, val1, val2):
    length, width = normalize(key, val1, val2)
    return engine(length, width)