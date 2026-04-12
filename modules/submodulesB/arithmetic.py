__ver__ = "0.3.0"
from utils.colors import colorize_feedback_type2, colorize
from .helper import allowed, replaced, clean
from system.settings.manager import Settings
import math

def usecase(signal: dict):
    settings = Settings()
    rounded = settings.get("precision")
    
    raw_action = " ".join(signal.get("action", []))
    
    # print(raw_action, "[!] CHECKPOINT")
    
    if not raw_action.strip():
        if settings.get("debugMode"):
            print(colorize_feedback_type2("X0", "Action cannot be empty"))
        return None
    
    prepared_action = replaced(raw_action)
    
    # print(prepared_action, "[!] CHECKPOINT")
    
    try:
        result = eval(prepared_action, {"__builtins__": {}}, allowed)
        return print(clean(result, rounded))
    except Exception as e:
        if settings.get("debugMode"):
            (colorize("TEXT_RED", f"Eval Error: {e}"))
        return None
