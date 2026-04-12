__ver__ = "0.3.3"
from utils.colors import colorize_feedback_type2
from system.settings.manager import Settings
from .version import version_debug
from utils.vlen import len_args

def handle(signal: dict):
    settings = Settings()
    if not settings.get("debugMode"):
        print(colorize_feedback_type2("X0", " Permission denied: debug mode required"))
        return None
    
    args = signal["args"]
    action = signal["action"]
    argument = len_args(args)
    
    if action == "version":
        if argument[0] == "--sync":
            return version_debug(None, None, argument[0])
        path, filtered = argument[0], argument[1]
        print(path, filtered)
        version_debug(path, filtered)
    return None