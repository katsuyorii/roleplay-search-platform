import uuid

from pydantic import BaseModel, Field

from announcements.schemas import AnnouncementResponseSchema


class AnnouncementAdminResponseSchema(AnnouncementResponseSchema):
    is_verify: bool
    moderator_message: str | None = Field(default=None)


class FandomResponseSchema(BaseModel):
    id: uuid.UUID
    name: str
    slug: str


class FandomCreateSchema(BaseModel):
    name: str = Field(max_length=256)


class FandomUpdateSchema(BaseModel):
    name: str | None = Field(default=None, max_length=256)


class TagResponseSchema(FandomResponseSchema):
    pass


class TagCreateSchema(FandomCreateSchema):
    pass


class NsfwFetishesTabooResponseSchema(FandomResponseSchema):
    pass


class NsfwFetishesTabooCreateSchema(FandomCreateSchema):
    pass