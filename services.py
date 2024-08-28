from models import Item
from repositories import ItemRepository
from typing import List


class ItemService:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    async def add_item(self, item: Item) -> str:
        return await self.repository.add_item(item)

    async def get_items(self) -> List[Item]:
        return await self.repository.get_items()
