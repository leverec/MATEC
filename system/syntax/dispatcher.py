__ver__ = "0.1.0"
import importlib
from system.loader import Load

config = Load()
modules = config.get("commands", "modules")

def dispatch_system(signal: dict):
    cmd = signal["command"]
    if cmd == "help":
        ...
    if cmd == "settings":
        from system.settings.usecase import handle
        return handle(signal) 
    if cmd == "debug":
        from system.debug.usecase import handle
        return handle(signal)
    if cmd == "matec":
        ...
    return

def dispatch_math(signal: dict):
    cmd = signal["command"]
    for category, commands in modules.items():
        if cmd in commands:
            try:
                module = importlib.import_module(f"modules.{category}.{cmd}.usecase")
                return module.handle(signal)
            except Exception as e:
                return print(e)
    return

def dispatch(signal: dict):
    if signal["type"] == "system":
        dispatch_system(signal)
    if signal["type"] == "math":
        dispatch_math(signal)
    return