__ver__ = "0.1.0"
from system.settings.manager import Settings
from modules.submodulesA.formatter import pretty_format
from modules.submodulesA.helper import length_checks
from .engine import (
    Circle_by_radius,
    Circle_by_diameter,
    Circle_by_circumference,
    Circle_by_area
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
    if signal["target"] == "r":
        pretty_format(Circle_by_radius(value1).result(), precision, unit)
        return None
    elif signal["target"] == "d":
        pretty_format(Circle_by_diameter(value1).result(), precision, unit)
        return None
    elif signal["target"] == "c":
        pretty_format(Circle_by_circumference(value1).result(), precision, unit)
        return None
    elif signal["target"] == "a":
        pretty_format(Circle_by_area(value1).result(), precision, unit)
        return None
    else:
        return None