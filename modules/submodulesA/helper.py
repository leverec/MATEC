__ver__ = "0.2.1"
def clean(n: float) -> int | float:
    if n.is_integer():
        return int(n)
    return n
def length_checks(n: list[str, str | None]) -> None | dict:
    if len(n) == 3:
        try:
            return {
                "status": "MN",
                "value": [float(n[0]), float(n[1]), float(n[2])]
            }
        except ValueError:
            return {"status": "X0"} 
    if len(n) == 2:
        try:
            return {
                "status": "TN",
                "value": [float(n[0]), float(n[1])]
            }
        except ValueError:
            return {"status": "X0"} 
    if len(n) == 1:
        try:
            return {
                "status": "SN",
                "value": float(n[0])
            }
        except ValueError:
            return {"status": "X0"}
    return {"status": "X0"}