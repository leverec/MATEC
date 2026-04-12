__ver__ = "0.3.2"
from utils.colors import colorize_feedback_type2, colorize
from .schema import SCHEMA, repair, generate
import yaml
import sys
import os

class Settings:
    FILE = "system/settings/settings.yml"
    def __init__(self):
        self._cli_debug = "-d" in sys.argv or "--debug" in sys.argv
        self.data = {}
        self.load()
        
    def _read(self):
        if not os.path.exists(self.FILE):
            return None
        try:
            with open(self.FILE, "r") as f:
                return yaml.safe_load(f)
        except Exception as e:
            if self._cli_debug:
                print(colorize_feedback_type2("X0", e))
            return None
            
    def _atomic_write(self, data):
        tmp_file = self.FILE + ".tmp"
        try:
            with open(tmp_file, "w") as f:
                yaml.dump(data, f, sort_keys=False)
            
            os.replace(tmp_file, self.FILE)
        except Exception as e:
            if os.path.exists(tmp_file):
                os.remove(tmp_file)
            if self._cli_debug:
                print(colorize_feedback_type2("X0", e))
                
    def load(self):
        raw_data = self._read()
        
        if raw_data is None:
            self.data = generate(SCHEMA)
        else:
            self.data = repair(raw_data, SCHEMA)
        
        self.data["debugMode"] = self._cli_debug
            
        self.save()
        return self.data
        
    def save(self):
        self._atomic_write(self.data)
        
    def get(self, key, default=None):
        if key == "debugMode":
            return self._cli_debug
        return self.data.get(key, default)
        
    def set(self, key, value):
        if key not in self.data:
            print(colorize_feedback_type2("X0", "This key cannot be found in settings"))
            return None
            
        if key == "debugMode":
            print(colorize_feedback_type2("X0", "Permission denied: this setting cannot be changed"))
            print(colorize_feedback_type2("NF", "debugMode is a setting that can only be changed by using the cli arguments"))
            return None
            
        try:
            try:
                value = int(value)
            except ValueError:
                value = str(value)
            self.data[key] = value
            self.data = repair(self.data, SCHEMA)
            
            if self.data.get(key) != value:
                if self._cli_debug:
                    print(colorize_feedback_type2("X0", f"The value for '{key}' is invalid according to schema rules"))
                    print(colorize_feedback_type2("NF", f"The value is invalid, the value for '{key}' will be reset to default"))
                    self.save()
                    return None
                print(colorize_feedback_type2("X0", "Invalid value"))
                self.save()
                return None
            self.save()
            print(colorize_feedback_type2("D1", f"'{key}' has been updated to '{value}'"))
            
        except Exception as e:
            print(colorize_feedback_type2("X0", "Something went wrong"))
            if self._cli_debug:
                print(colorize("TEXT_RED", f"FATAL: {e}"))