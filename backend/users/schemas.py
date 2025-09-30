import uuid

from pydantic import BaseModel, EmailStr

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