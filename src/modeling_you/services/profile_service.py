from datetime import datetime, timezone
from typing import Dict

from modeling_you.repositories import profile_repository
from modeling_you.schemas import profile_schema


class ProfileService:

    def __init__(self):
        # directly create, not DI
        self.repo = profile_repository.ProfileRepository()

    async def update_profile(
        self, profile_update: profile_schema.ProfileUpdateRequest, user_id: str
    ) -> profile_schema.ProfileUpdateResponse:
        # update dict for the repo
        update: Dict = {}
        if profile_update.basic_info:
            update.update(
                {
                    f"basic_info.{k}": v
                    for k, v in profile_update.basic_info.model_dump(
                        exclude_none=True
                    ).items()
                }
            )
        if profile_update.preference:
            update.update(
                {
                    f"preference.{k}": v
                    for k, v in profile_update.preference.model_dump(
                        exclude_none=True
                    ).items()
                }
            )

        if not update:
            return None

        update["metadata.last_update"] = datetime.now(timezone.utc)

        await self.repo.update(user_id, update)

        return profile_schema.ProfileUpdateResponse(message="OK")


1
