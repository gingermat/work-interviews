from typing import Dict, List

from aiomongo import AioMongoClient

from app.models import InventoryModel


DEFAULT_BATCH_SIZE = 10


class InventoryRepository:
    def __init__(self, client: AioMongoClient, collection: str) -> None:
        db = client.get_default_database()
        self._collection = getattr(db, collection)

    async def insert(self, model: InventoryModel) -> None:
        await self._collection.insert_one(model.to_dict())

    async def fetch_many(self, condition: Dict, offset: int = 0, limit: int = 50) -> List[InventoryModel]:
        models = []

        async with self._collection.find(condition).batch_size(DEFAULT_BATCH_SIZE).skip(offset).limit(limit) as cursor:
            async for item in cursor:
                item.pop("_id", None)
                models.append(InventoryModel(**item))

        return models
