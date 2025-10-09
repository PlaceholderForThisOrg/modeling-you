from fastapi import APIRouter, Depends, HTTPException

from modeling_you.auth import verify_token
from modeling_you.schemas import profile_schema
from modeling_you.services import profile_service
from modeling_you.types import Payload

router = APIRouter(
    prefix="/api/v1/profiles",
    tags=["profiles"],
)


@router.patch("/{user_id}", response_model=profile_schema.ProfileUpdateResponse)
async def update_profile(
    # user_id: str,
    profile_update_request: profile_schema.ProfileUpdateRequest,
    payload: Payload = Depends(verify_token),
):
    # create the service
    service = profile_service.ProfileService()
    response = await service.update_profile(profile_update_request, payload["sub"])
    if not response:
        raise HTTPException(status_code=404, detail="Profile not found")
    return response
