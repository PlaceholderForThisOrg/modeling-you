from typing import Dict

from modeling_you.db import collection, database


class ProfileRepository:
    def __init__(self):
        self.database = database
        self.collection = collection

    async def update(self, user_id: str, update_profile: Dict):
        filter = {"user_id": user_id}
        update = {"$set": update_profile}
        # if doesn't exist -> create
        result = await self.collection.update_one(
            filter=filter, update=update, upsert=True
        )

        if result.matched_count == 0:
            return None

        return await self.collection.find_one(filter=filter)
