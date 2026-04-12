__ver__ = "0.3.0"

def len_float(value: list[str]):
    if value is None: return {"status": "X0"}
    if len(value) == 3:
        try:
            return {"status": "MN","value": [float(value[0]), float(value[1]), float(value[2])]}
        except ValueError:
            return {"status": "X0"} 
    if len(value) == 2:
        try:
            return {"status": "TN","value": [float(value[0]), float(value[1])]}
        except ValueError:
            return {"status": "X0"} 
    if len(value) == 1:
        try:
            return {"status": "SN","value": float(value[0])}
        except ValueError:
            return {"status": "X0"}
    return {"status": "X0"}

def len_args(argument: list[str]):
    if argument is None: return [None, None]
    if len(argument) == 1 : return [argument[0], None]
    return [argument[0] if argument[0] else None,argument[1] if argument[1] else None]