__ver__ = "0.1.0"
from system.settings.manager import Settings
from modules.submodulesA.formatter import pretty_format
from modules.submodulesA.helper import length_checks
from .engine import (
    Rectangle_by_base,
    Rectangle_by_diagonal,
    Rectangle_by_perimeter,
    Rectangle_by_area
    )

def handle(signal):
    #####################
    settings = Settings()
    unit = settings.get("unit")
    precision = settings.get("precision")
    # ↑ from settings ↑ ↓ from helper ↓
    value = length_checks(signal["values"])
    if value["status"] != "M1":
        return None
    value_1, value_2 = value["value"][0], value["value"][1]
    #####################
    if signal["target"] == "b":
        pretty_format(Rectangle_by_base(value_1, value_2).result(), precision, unit)
        return None
    elif signal["target"] == "d":
        pretty_format(Rectangle_by_diagonal(value_1, value_2).result(), precision, unit)
        return None
    elif signal["target"] == "p":
        pretty_format(Rectangle_by_perimeter(value_1, value_2).result(), precision, unit)
        return None
    elif signal["target"] == "a":
        pretty_format(Rectangle_by_area(value_1, value_2).result(), precision, unit)
        return None
    else:
        return None