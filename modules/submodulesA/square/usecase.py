__ver__ = "0.3.2"
from modules.submodulesA.formatter import pretty_format
from system.settings.manager import Settings
from utils.vlen import len_float
from .engine import solve

def handle(signal):
    #####################
    settings = Settings()
    unit = settings.get("unit")
    precision = settings.get("precision")
    # ↑ from settings ↑ ↓ from helper ↓
    value = len_float(signal["values"])
    if value["status"] != "SN":
        if settings.get("debugMode"):
            print(colorize_feedback_type2("X0", "Value length has to be 1 AND NOT \033[34mNone\033[0m"))
        return None
    val = value["value"]
    #####################
    key = signal["target"]
    if key in ("s", "d", "p", "a"):
        return pretty_format(solve(key, val), precision, unit)
    else:
        if settings.get("debugMode"):
            print(colorize_feedback_type2("X0", "Invalid arguments"))
        return None