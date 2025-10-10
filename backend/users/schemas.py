import uuid

from pydantic import BaseModel, EmailStr, Field

from datetime import datetime, date

from announcements.schemas import AnnouncementOrientation, AnnouncementGender


class UserResponseSchema(BaseModel):
    id: uuid.UUID
    email: EmailStr
    username: str | None
    role: str
    gender: str | None
    date_of_birth: date | None
    last_login: datetime | None
    is_active: bool
    is_mailing: bool
    created_at: datetime
    updated_at: datetime


class UserUpdateSchema(BaseModel):
    username: str | None = Field(default=None, max_length=255)
    gender: str | None = Field(default=None)
    date_of_birth: date | None = Field(default=None)
    is_mailing: bool | None = Field(default=None)

class AnnouncementCreateSchema(BaseModel):
    orientation: AnnouncementOrientation | None = Field(default=None)
    gender: AnnouncementGender | None = Field(default=None)
    description: str
    fandoms: list[uuid.UUID] | None = Field(default=None)
    tags: list[uuid.UUID] | None = Field(default=None)
    is_crossgender: bool
    is_active: bool = Field(default=True)
    is_anonymously: bool = Field(default=True)
    is_nsfw: bool = Field(default=False)
    nsfw_fetishes: list[uuid.UUID] | None = Field(default=None)
    nsfw_taboo: list[uuid.UUID] | None = Field(default=None)


class AnnouncementUpdateSchema(AnnouncementCreateSchema):
    description: str | None = Field(default=None)
    is_crossgender: bool | None = Field(default=None)
    is_active: bool | None = Field(default=None)
    is_anonymously: bool | None = Field(default=None)
    is_nsfw: bool | None = Field(default=None)