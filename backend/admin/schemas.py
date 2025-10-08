import uuid

from pydantic import BaseModel, Field


class FandomResponseSchema(BaseModel):
    id: uuid.UUID
    name: str
    slug: str


class FandomCreateSchema(BaseModel):
    name: str = Field(max_length=256)


class TagResponseSchema(FandomResponseSchema):
    pass


class TagCreateSchema(FandomCreateSchema):
    pass


class NsfwFetishesTabooResponseSchema(FandomResponseSchema):
    pass


class NsfwFetishesTabooCreateSchema(FandomCreateSchema):
    pass