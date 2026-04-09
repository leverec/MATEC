__ver__ = "0.2.0"
from .helper import clean

def pretty_format(data: dict, rounded: int, unit: str) -> None:
    max_len = max(len(str(k))for k in data)
    for key, value in data.items():
        value = round(value, rounded)
        if key == "area":
            _unit = f"{unit}²"
        else:
            _unit = unit
        print(f"{key.capitalize():<{max_len}} : {clean(value)}{_unit}")
