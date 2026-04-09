__ver__ = "0.2.0"
from system.settings.manager import Settings
from modules.submodulesA.formatter import pretty_format
from modules.submodulesA.helper import length_checks
from .engine import solve

def handle(signal):
    #####################
    settings = Settings()
    unit = settings.get("unit")
    precision = settings.get("precision")
    # ↑ from settings ↑ ↓ from helper ↓
    value = length_checks(signal["values"])
    if value["status"] not in ("TN", "MN"):
        return None
    val1, val2 = value["value"][0], value["value"][1]
    #####################
    key = signal["target"]
    # MultiNum Fork ↓
    if value["status"] == "MN":
        val1, val2, val3 = value["value"][0], value["value"][1], value["value"][2]
        if key == "p":
            return pretty_format(solve(key, val1, val2, val3), precision, unit)
    # MultiNum Fork ↑
    if key in ("b", "h", "a"):
        return pretty_format(solve(key, val1, val2), precision, unit)
    return None