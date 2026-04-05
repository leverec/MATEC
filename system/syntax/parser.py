__ver__ = "0.1.1"
from system.loader import Load

config = Load()
system_commands = config.get("commands", "system")

def tokenize(syntax):
    return syntax.strip().split()

def parse(syntax):
    tokens = tokenize(syntax)
    if not tokens:
        return {"type": "unknown"}
    cmd = tokens[0]
    if len(tokens) == 1 and cmd == "help":
        return {
            "type": "system",
            "command": "help"
        }
    if len(tokens) == 1 and cmd == "exit":
        return {
            "type": "system",
            "command": "exit"
        }
    if cmd in system_commands:
        return {
            "type": "system",
            "command": tokens[0],
            "action": tokens[1] if len(tokens) > 1 else None,
            "args": tokens[2:] if len(tokens) > 2 else None
        }
    if len(tokens) > 1:
        return {
            "type": "math",
            "command": tokens[0],
            "target": tokens[1],
            "values": tokens[2:]
        }
    return {"type": "unknown"}