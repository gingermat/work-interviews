import json
from typing import Dict


class ModelException(Exception):
    pass


class InventoryModel:
    def __init__(self, component: str, description: str, model: str, country: str = "USA", **_: Dict) -> None:
        self.component = component
        self.description = description
        self.model = model
        self.country = country

    @classmethod
    def from_json(cls, data: str) -> "InventoryModel":
        """Create `InventoryModel` from json-data string"""
        try:
            parsed = json.loads(data)
        except json.decoder.JSONDecodeError:
            raise ModelException(f"Invalid JSON data: {data}")

        if parsed.get("country") in {"", None}:
            parsed.pop("country", None)

        try:
            return cls(**parsed)
        except TypeError as exc:
            raise ModelException(f"Cannot create model: {exc}. Data: {parsed}")

    def to_dict(self) -> dict:
        """Presents `InventoryModel` class as dict"""
        return vars(self)
