__ver__ = "0.2.1"
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
    if value["status"] != "SN":
        return None
    val = value["value"]
    #####################
    key = signal["target"]
    if key in ("r", "d", "c", "a"):
        return pretty_format(solve(key, val), precision, unit)
    return None