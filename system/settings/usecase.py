__ver__ = "0.3.1"
from utils.colors import colorize_feedback_type2
from utils.vlen import len_args
from .manager import Settings

def handle(signal):
    #####################
    settings = Settings()
    action = signal["action"]
    #####################
    if action == "get":
        key = len_args(signal["args"])[0]
        if key is None:
            if settings.get("debugMode"):
                print(colorize_feedback_type2("X0", "Key is \033[0;95mNone\033[0m"))
            return None
        return print(f"{key}: {settings.get(key)}")
    
    elif action == "set":
        key, value = len_args(signal["args"])
        if key is None or value is None:
            if settings.get("debugMode"):
                print(colorize_feedback_type2("X0", "Key or Value is \033[0;95mNone\033[0m"))
            return None
        settings.set(key, value)
        
    elif action == "show":
        data = settings.load()
        max_len = max(len(str(k))for k in data)
        for key, value in data.items():
            print(f"{key:<{max_len}} : {value}")