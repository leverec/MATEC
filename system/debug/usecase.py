__ver__ = "0.2.2"
from .scanner import scan
from .sync import sync
from .helper import length_checks

def handle(signal: dict) -> None:
    args = signal["args"]
    action = signal["action"]
    argument = length_checks(args)
    
    if action == "version":
        if argument[0] is not None and argument[0] == "--sync":
            return sync()
        path, filtered = argument[0], argument[1]
        scan(path, filtered)