__ver__ = "0.3.2"
def clean(n: float) -> int | float:
    if n.is_integer():
        return int(n)
    return n