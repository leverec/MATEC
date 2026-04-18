__ver__ = "0.3.1"
import math
import re

def replaced(text):
    text = text.lower().replace(" ", "")
    text = text.replace("π", "pi")
    text = re.sub(r'√(\d+\.?\d*)', r'sqrt(\1)', text)
    text = text.replace("√(", "sqrt(")
    text = re.sub(r'(?<![a-z])e(?=[0-9p\(])', 'e*', text)
    text = re.sub(r'(\d)e(?![a-z])', r'\1*e', text)
    text = re.sub(r'(\d)pi', r'\1*pi', text)
    text = re.sub(r'pi(\d|[a-z\(])', r'pi*\1', text)
    text = text.replace("*x", "*")
    text = text.replace("x*", "*")
    pattern_x = r'(?<=[0-9e i\)])x(?=[0-9ep s m\(\[])'
    text = re.sub(pattern_x, '*', text)
    replacements = {
        "^": "**",
        ":": "/",
        "÷": "/",
        "×": "*"
    }
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
