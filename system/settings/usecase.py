__ver__ = "0.1.0"
from .manager import Settings

def valid_get(key):
    if key is None or len(key) != 1:
        return None
    return key[0]

def handle(signal):
    #####################
    settings = Settings()
    action = signal["action"]
    #####################
    if action == "get":
        key = valid_get(signal["args"]).lower()
        if key is None:
            return None
        print(f"{key}: {settings.get(key)}")
    elif action == "show":
        data = settings.load()
        max_len = max(len(str(k))for k in data)
        for key, value in data.items():
            print(f"{key.capitalize():<{max_len}} : {value}")