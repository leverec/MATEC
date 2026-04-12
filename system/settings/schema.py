__ver__ = "0.3.0"
SCHEMA = {
    "unit": {
        "type": str,
        "default": "cm",
        "allowed": ["mm", "cm", "dm", "m", "km"]
    },
    "precision": {
        "type": int,
        "default": 2,
        "min": 0,
        "max": 15
    },
    "showUnit": {
        "type": bool,
        "default": True
    },
    "debugMode": {
        "type": bool,
        "default": False
    }
}


def validate(data: dict, schema: dict) -> bool:
    if not isinstance(data, dict):
        return False
    for key, rules in schema.items():
        if key not in data:
            return False
        value = data[key]
        if not isinstance(value, rules["type"]):
            return False
        if "allowed" in rules and value not in rules["allowed"]:
            return False
        if "min" in rules and value < rules["min"]:
            return False
        if "max" in rules and value > rules["max"]:
            return False
    return True


def repair(data: dict, schema: dict):
    fixed = {}
    if not isinstance(data, dict):
        data = {}
    for key, rules in schema.items():
        value = data.get(key, rules["default"])
        if not isinstance(value, rules["type"]):
            value = rules["default"]
        if "allowed" in rules and value not in rules["allowed"]:
            value = rules["default"]
        if "min" in rules and value < rules["min"]:
            value = rules["default"]
        if "max" in rules and value > rules["max"]:
            value = rules["default"]
        fixed[key] = value
    return fixed


def generate(schema: dict) -> dict:
    return {
        key: rules["default"]
        for key, rules in schema.items()
    }