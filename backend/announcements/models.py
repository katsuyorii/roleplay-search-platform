import uuid

from sqlalchemy import String, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from enum import Enum

from core.models.base import BaseModel


announcements_fandoms = Table(
    'announcements_fandoms',
    BaseModel.metadata,
    Column('annnouncement_id', ForeignKey('announcements.id'), primary_key=True),
    Column('fandom_id', ForeignKey('fandoms.id'), primary_key=True),
)

announcements_tags = Table(
    'announcements_tags',
    BaseModel.metadata,
    Column('annnouncement_id', ForeignKey('announcements.id'), primary_key=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True),
)

announcements_nsfw_fetishes = Table(
    'announcements_nsfw_fetishes',
    BaseModel.metadata,
    Column('annnouncement_id', ForeignKey('announcements.id'), primary_key=True),
    Column('nsfw_fetish_id', ForeignKey('nsfw_fetishes_taboo.id'), primary_key=True),
)

announcements_nsfw_taboo = Table(
    'announcements_nsfw_taboo',
    BaseModel.metadata,
    Column('annnouncement_id', ForeignKey('announcements.id'), primary_key=True),
    Column('nsfw_taboo_id', ForeignKey('nsfw_fetishes_taboo.id'), primary_key=True),
)


class AnnouncementOrientation(str, Enum):
    GET = 'get'
    SLASH = 'slash'
    FEMSLASH = 'femslash'
    DZHEN = 'dzhen'


class AnnouncementGender(str, Enum):
    MALE = 'male'
    FEMALE = 'female'
    ANOTHER = 'another'


class NsfwFetishTabooModel(BaseModel):
    __tablename__ = 'nsfw_fetishes_taboo'

    name: Mapped[str] = mapped_column(String(256), unique=True)
    slug: Mapped[str] = mapped_column(String(256), unique=True, index=True)


class FandomModel(BaseModel):
    __tablename__ = 'fandoms'

    name: Mapped[str] = mapped_column(String(256), unique=True)
    slug: Mapped[str] = mapped_column(String(256), unique=True, index=True)


class TagModel(BaseModel):
    __tablename__ = 'tags'

    name: Mapped[str] = mapped_column(String(256), unique=True)
    slug: Mapped[str] = mapped_column(String(256), unique=True, index=True)


class AnnouncementModel(BaseModel):
    __tablename__ = 'announcements'

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    orientation: Mapped[str] = mapped_column(String(8), nullable=True)
    gender: Mapped[str] = mapped_column(String(7), nullable=True)
    description: Mapped[str]
    # posters_urls: List[] (M2M)

    fandoms: Mapped[list[FandomModel]] = relationship(secondary=announcements_fandoms)
    tags: Mapped[list[TagModel]] = relationship(secondary=announcements_tags)

    is_crossgender: Mapped[bool] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    is_anonymously: Mapped[bool] = mapped_column(default=True)
    is_verify: Mapped[bool] = mapped_column(default=False)

    is_nsfw: Mapped[bool] = mapped_column(default=False)
    nsfw_fetishes: Mapped[list[NsfwFetishTabooModel]] = relationship(secondary=announcements_nsfw_fetishes)
    nsfw_taboo: Mapped[list[NsfwFetishTabooModel]] = relationship(secondary=announcements_nsfw_taboo)

    moderator_message: Mapped[str] = mapped_column(nullable=True)