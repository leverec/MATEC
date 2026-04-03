__ver__ = "0.1.0"
from system.settings.manager import Settings
from modules.submodulesA.formatter import pretty_format
from modules.submodulesA.helper import length_checks
from .engine import (
    Square_by_side,
    Square_by_diagonal,
    Square_by_perimeter,
    Square_by_area
    )

def handle(signal):
    #####################
    settings = Settings()
    unit = settings.get("unit")
    precision = settings.get("precision")
    # ↑ from settings ↑ ↓ from helper ↓
    value = length_checks(signal["values"])
    if value["status"] != "S0":
        return None
    value1 = value["value"]
    #####################
    if signal["target"] == "s":
        pretty_format(Square_by_side(value1).result(), precision, unit)
        return None
    elif signal["target"] == "d":
        pretty_format(Square_by_diagonal(value1).result(), precision, unit)
        return None
    elif signal["target"] == "p":
        pretty_format(Square_by_perimeter(value1).result(), precision, unit)
        return None
    elif signal["target"] == "a":
        pretty_format(Square_by_area(value1).result(), precision, unit)
        return None
    else:
        return None