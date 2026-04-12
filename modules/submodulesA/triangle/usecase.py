__ver__ = "0.3.1"
from modules.submodulesA.formatter import pretty_format
from utils.colors import colorize_feedback_type2
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
    if value["status"] != "TN":
        if settings.get("debugMode"):
            print(colorize_feedback_type2("X0", "Value length has to be 2 AND NOT \033[35mNone\033[0m"))
        return None
    val1, val2 = value["value"][0], value["value"][1]
    #####################
    key = signal["target"]
    if key in ("b", "h", "a"):
        return pretty_format(solve(key, val1, val2), precision, unit)
    else:
        if settings.get("debugMode"):
            print(colorize_feedback_type2("X0", "Invalid arguments"))
        return None