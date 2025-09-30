import uuid

from pydantic import BaseModel, EmailStr, Field

from datetime import datetime, date


class UserResponseSchema(BaseModel):
    id: uuid.UUID
    email: EmailStr
    username: str | None
    role: str
    gender: str | None
    date_of_birth: date | None
    last_login: datetime
    is_active: bool
    is_mailing: bool
    created_at: datetime
    updated_at: datetime


class UserUpdateSchema(BaseModel):
    username: str | None = Field(default=None, max_length=255)
    gender: str | None = Field(default=None)
    date_of_birth: date | None = Field(default=None)
    is_mailing: bool | None = Field(default=None)