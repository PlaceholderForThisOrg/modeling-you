from typing import List, Optional

from pydantic import BaseModel


class BasicInfo(BaseModel):
    nickname: Optional[str] = None
    timezone: Optional[str] = None
    age: Optional[int] = None
    level: Optional[str] = None
    goal: Optional[List[str]] = None
    native_language: Optional[str] = None
    preferred_practice_time: Optional[str] = None


class Preference(BaseModel):
    preferred_topics: Optional[List[str]] = None
    blocked_topics: Optional[List[str]] = None
    preferred_learning_style: Optional[str] = None
    difficulty_preference: Optional[str] = None
    content_maturity: Optional[str] = None


class ProfileUpdateRequest(BaseModel):
    basic_info: Optional[BasicInfo] = None
    preference: Optional[Preference] = None


class ProfileUpdateResponse(BaseModel):
    message: str = "OK"
