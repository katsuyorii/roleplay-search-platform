import uuid

from pydantic import BaseModel, Field


class FandomSchema(BaseModel):
    id: uuid.UUID
    name: str


class TagSchema(BaseModel):
    id: uuid.UUID
    name: str


class NsfwFetishSchema(BaseModel):
    id: uuid.UUID
    name: str


class NsfwTabooSchema(BaseModel):
    id: uuid.UUID
    name: str


class AnnouncementResponseSchema(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    orientation: str | None = Field(default=None)
    gender: str | None = Field(default=None)
    description: str
    fandoms: list[FandomSchema] | None = Field(default=None)
    tags: list[TagSchema] | None = Field(default=None)
    is_crossgender: bool 
    is_active: bool
    is_anonymously: bool
    is_verify: bool
    is_nsfw: bool
    nsfw_fetishes: list[NsfwFetishSchema] | None = Field(default=None)
    nsfw_taboo: list[NsfwTabooSchema] | None = Field(default=None)


class AnnouncementCreateSchema(BaseModel):
    orientation: str | None = Field(default=None)
    gender: str | None = Field(default=None)
    description: str
    fandoms: list[uuid.UUID] | None = Field(default=None)
    tags: list[uuid.UUID] | None = Field(default=None)
    is_crossgender: bool
    is_active: bool = Field(default=True)
    is_anonymously: bool = Field(default=True)
    is_nsfw: bool = Field(default=False)
    nsfw_fetishes: list[uuid.UUID] | None = Field(default=None)
    nsfw_taboo: list[uuid.UUID] | None = Field(default=None)


class AnnouncementUpdateSchema(BaseModel):
    orientation: str | None = Field(default=None)
    gender: str | None = Field(default=None)
    description: str | None = Field(default=None)
    fandoms: list[uuid.UUID] | None = Field(default=None)
    tags: list[uuid.UUID] | None = Field(default=None)
    is_crossgender: bool | None = Field(default=None)
    is_active: bool | None = Field(default=None)
    is_anonymously: bool | None = Field(default=None)
    is_nsfw: bool | None = Field(default=None)
    nsfw_fetishes: list[uuid.UUID] | None = Field(default=None)
    nsfw_taboo: list[uuid.UUID] | None = Field(default=None)