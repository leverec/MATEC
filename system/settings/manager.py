__ver__ = "0.2.1"
import yaml
import os
import shutil
from .schema import SCHEMA, validate, repair, generate

class Settings:
    SETTINGS_FILE: str = "system/settings/settings.yml"
    BACKUP_FILE: str = "system/settings/backup.yml"
    DEFAULT_FILE: str = "system/settings/default.yml"
    def __init__(self):
        self.data = {}
        self.load()
    def _read(self, path):
        if not os.path.exists(path):
            return None
        try:
            with open(path, "r") as f:
                return yaml.safe_load(f)
        except Exception:
            return None
    def _write(self, path, data):
        with open(path, "w") as f:
            yaml.dump(data, f, sort_keys=False)
    def load(self):
        # try settings
        data = self._read(self.SETTINGS_FILE)
        if validate(data, SCHEMA):
            self.data = data
            return self.data
        if data is not None:
            data = repair(data, SCHEMA)
            self.data = data
            self._write(self.SETTINGS_FILE, data)
            return self.data
        # then try backup
        data = self._read(self.BACKUP_FILE)
        if validate(data, SCHEMA):
            self.data = data
            self._write(self.SETTINGS_FILE, data)
            return self.data
        if data is not None:
            data = repair(data, SCHEMA)
            self.data = data
            self._write(self.SETTINGS_FILE, data)
            return self.data
        # and then try default
        data = self._read(self.DEFAULT_FILE)
        if validate(data, SCHEMA):
            self.data = data
        elif data is not None:
            self.data = repair(data, SCHEMA)
        else:
            # last, schema generate
            self.data = generate(SCHEMA)
        # recreate files
        self._write(self.SETTINGS_FILE, self.data)
        self._write(self.BACKUP_FILE, self.data)
        self._write(self.DEFAULT_FILE, self.data)
        return self.data
    def save(self):
        if os.path.exists(self.SETTINGS_FILE):
            shutil.copy(self.SETTINGS_FILE, self.BACKUP_FILE)
        self._write(self.SETTINGS_FILE, self.data)
    def get(self, key, default=None):
        return self.data.get(key, default)
    def set(self, key, value):
        self.data[key] = value
        self.data = repair(self.data, SCHEMA)
        self.save()
    def reload(self):
        return self.load()