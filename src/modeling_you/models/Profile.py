from datetime import datetime
from typing import Dict, List

from pydantic import BaseModel, Field

from .ObjectId import PyObjectId


class BasicInfo(BaseModel):
    nickname: str
    timezone: str
    age: int
    level: str
    goal: List[str]
    native_language: str
    preferred_practice_time: str


class Preference(BaseModel):
    preferred_topics: List[str]
    blocked_topics: List[str]
    preferred_learning_style: str
    difficulty_preference: str
    content_maturity: str


class ReadingPattern(BaseModel):
    average_duration: int
    average_scroll_depth: int
    highlight_rate: int


class RecentInfo(BaseModel):
    interest_topics: Dict[str, int]
    reading_patterns: ReadingPattern
    recent_keywords: List[str]
    recent_domains: List[str]


class LanguageAbility(BaseModel):
    vocab_size_estimate: int


class MetaData(BaseModel):
    version: str = "v1.0"
    last_update: datetime


class Profile(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: str
    basic_info: BasicInfo
    preference: Preference
    recent_info: RecentInfo
    ability: LanguageAbility
    metadata: MetaData
