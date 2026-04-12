__ver__ = "0.3.1"
from system.settings.manager import Settings
from utils.colors import colorize
from system.loader import Load
import importlib

settings = Settings()

config = Load()
modules = config.get("commands", "modules")
system_modules = config.get("commands", "system")

CMD_TO_CAT = {cmd: cat for cat, cmds in modules.items() for cmd in cmds}

def dispatch_system(signal: dict):
    cmd = signal["command"]
    if cmd in system_modules:
        if cmd in ("q", "exit")   : return "exit"  # it does nothing
        if cmd in ("cls", "clear"): return "clear" # it's just making sure that it won't go into that importlib
        try:
            path = f"system.{cmd}.usecase"
            module = importlib.import_module(path)
            return module.handle(signal)
        except Exception as e:
            if settings.get("debugMode"):
                print(colorize("TEXT_RED", f"FATAL: {e}"))
            return None
    return None

def dispatch_geometry(signal: dict):
    cmd = signal["command"]
    category = CMD_TO_CAT.get(cmd)
    if category:
        try:
            path = f"modules.{category}.{cmd}.usecase"
            module = importlib.import_module(path)
            return module.handle(signal)
        except Exception as e:
            if settings.get("debugMode"):
                print(colorize("TEXT_RED", f"FATAL: {e}"))
            return None
    return None

def dispatch_arithmetic(signal: dict):
    try:
        from modules.submodulesB.arithmetic import usecase
        return usecase(signal)
    except Exception as e:
        if settings.get("debugMode"):
            print(colorize("TEXT_RED", f"FATAL: {e}"))
        return None
    return None

def dispatch(signal: dict):
    _type = signal["type"]
    if _type == "system"    : dispatch_system(signal)
    if _type == "geometry"  : dispatch_geometry(signal)
    if _type == "arithmetic": dispatch_arithmetic(signal)
    return