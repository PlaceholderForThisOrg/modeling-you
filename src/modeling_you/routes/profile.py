from fastapi import APIRouter, Depends

from modeling_you.auth import verify_token
from modeling_you.schemas import Test, profile_schema
from modeling_you.types import Payload

router = APIRouter(
    prefix="/api/v1/profiles",
    tags=["profiles"],
)


@router.patch("/", response_model=Test)
async def update_profile(
    profile_update_request: profile_schema.ProfileUpdateRequest,
    payload: Payload = Depends(verify_token),
):
    return Test(message="So far so good")
