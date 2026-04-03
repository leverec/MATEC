__ver__ = "0.1.0"

def clean(n: float) -> int | float:
    if n.is_integer():
        return int(n)
    return n
def length_checks(n: list[str, str | None]) -> None | dict:
    if len(n) == 2:
        try:
            n1, n2 = float(n[0]), float(n[1])
        except ValueError:
            return {"status": "X0"} 
        return {
            "status": "M1",
            "value": [n1, n2]
        }
    if len(n) == 1:
        try:
            n1 = float(n[0])
        except ValueError:
            return {"status": "X0"}
        return {
            "status": "S0",
            "value": n1
        }
    return {"status": "X0"}