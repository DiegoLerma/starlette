from models import Item
from typing import List


class ItemRepository:
    def __init__(self, db):
        self.collection = db.get_collection("items")

    async def add_item(self, item: Item) -> str:
        item_dict = item.model_dump(by_alias=True)
        if item_dict["_id"] is None:
            del item_dict["_id"]
        result = await self.collection.insert_one(item_dict)
        return str(result.inserted_id)

    async def get_items(self) -> List[Item]:
        items_cursor = self.collection.find()
        items = await items_cursor.to_list(length=100)

        # Convertir _id de ObjectId a string antes de crear instancias de Item
        return [
            Item(**{**item, "_id": str(item["_id"])}) for item in items
        ]
