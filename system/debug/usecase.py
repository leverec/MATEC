__ver__ = "0.1.0"
from .scanner import scan

def handle(signal):
    if signal["action"] == "version":
        scan(signal["args"])