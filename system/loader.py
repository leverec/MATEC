__ver__ = "0.2.0"
import yaml
from pathlib import Path

class Load:
    def __init__(self):
        self.root = Path(__file__).resolve().parents[1]
        self.file = self.root / "system/config.yml"
        with open(self.file, "r") as f:
            self.data = yaml.safe_load(f)
    def get(self, *keys, default=None):
        value = self.data
        try:
            for key in keys:
                value = value[key]
            return value
        except KeyError:
            return default