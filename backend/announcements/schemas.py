import uuid

from pydantic import BaseModel, Field

from .models import AnnouncementOrientation, AnnouncementGender


class FandomSchema(BaseModel):
    id: uuid.UUID
    name: str
    slug: str


class TagSchema(BaseModel):
    id: uuid.UUID
    name: str
    slug: str


class NsfwFetishSchema(BaseModel):
    id: uuid.UUID
    name: str
    slug: str


class NsfwTabooSchema(BaseModel):
    id: uuid.UUID
    name: str
    slug: str


class AnnouncementResponseSchema(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    orientation: AnnouncementOrientation | None = Field(default=None)
    gender: AnnouncementGender | None = Field(default=None)
    description: str
    fandoms: list[FandomSchema] | None = Field(default=None)
    tags: list[TagSchema] | None = Field(default=None)
    is_crossgender: bool 
    is_active: bool
    is_anonymously: bool
    is_nsfw: bool
    nsfw_fetishes: list[NsfwFetishSchema] | None = Field(default=None)
    nsfw_taboo: list[NsfwTabooSchema] | None = Field(default=None)