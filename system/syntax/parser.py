__ver__ = "0.3.2"
from system.loader import Load
from enum import Enum

config = Load()
system_commands = config.get("commands", "system")
geometry_commands = config.get("modules", "geometry")

class CommandType(Enum):
    SYSTEM = "system"
    GEOMETRY   = "geometry"
    ARITHMETIC = "arithmetic"
    UNKNOWN = "unknown"

def tokenize(syntax: str) -> list[str]:
    if not isinstance(syntax, str):
        return []
    return syntax.strip().split()

def _classify(tokens: list[str]) -> CommandType:
    if not tokens:
        return CommandType.UNKNOWN
    cmd = tokens[0]
    if cmd in system_commands:
        return CommandType.SYSTEM
    if cmd in geometry_commands:
        return CommandType.GEOMETRY
    return CommandType.ARITHMETIC

def parse(syntax: str) -> dict:
    tokens = tokenize(syntax)
    kind = _classify(tokens)
    
    if kind == CommandType.SYSTEM:
        return {
            "type"   : CommandType.SYSTEM.value,
            "command": tokens[0],
            "action" : tokens[1] if len(tokens) > 1 else None,
            "args"   : tokens[2:] if len(tokens) > 2 else None,
        }
    if kind == CommandType.GEOMETRY:
        return {
            "type"   : CommandType.GEOMETRY.value,
            "command": tokens[0],
            "target" : tokens[1],
            "values" : tokens[2:] if len(tokens) > 2 else None,
        }
    if kind == CommandType.ARITHMETIC:
        return {
            "type"   : CommandType.ARITHMETIC.value,
            "command": "arithmetic",
            "action" : tokens[0:]
        }
    return {
        "type"   : CommandType.UNKNOWN.value,
        "command": tokens[0] if tokens else None,
    }