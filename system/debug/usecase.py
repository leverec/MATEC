__ver__ = "0.1.1"
from .scanner import scan

def scanner_len(args: list) -> tuple[None | str, None | str]:
    if args is None:
        return None, None
    if len(args) > 1:
        return args[0], args[1]
    if len(args) == 1:
        return args[0], None
    return None, None

def handle(signal: dict) -> None:
    if signal["action"] == "version":
        path, filtered = scanner_len(signal["args"])
        scan(path, filtered)