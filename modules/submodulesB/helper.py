import math
import re

def replaced(text):
    text = text.lower()
    text = text.replace("π", " pi ")
    text = re.sub(r'√(\d+\.?\d*)', r'sqrt(\1)', text)
    text = text.replace("√(", "sqrt(")
    text = re.sub(r'(\d|pi|\))\s*x\s*(\d|pi|\()', r'\1 * \2', text)
    text = "".join(text.split())
    
    replacements = {"^": "**", ":": "/", "÷": "/", "×": "*"}
    for old, new in replacements.items():
        text = text.replace(old, new)
        
    return text


def root(number, n=2):
    return number ** (1/n)


def clean(n: float, rounded) -> int | float:
    if isinstance(n, float) and n.is_integer():
        return int(n)
    return round(n, rounded)

allowed = {
    "sqrt": math.sqrt,
    "cbrt": math.cbrt,
    "pi": math.pi,
    "e": math.e,
    "power": pow,
    "pow": pow,
    "max": max,
    "min": min,
    "root": root
}
