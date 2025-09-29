import json

from abc import ABC, abstractmethod

class SaveData(ABC):
    @abstractmethod
    def save(self, data, filename):
        pass


class SaveToJSON(SaveData):
    def save(self, data, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

