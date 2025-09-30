import uuid

from sqlalchemy import String, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from enum import Enum

from core.models.base import BaseModel


annnouncements_fandoms = Table(
    'annnouncements_fandoms',
    BaseModel.metadata,
    Column('annnouncement_id', ForeignKey('announcements.id'), primary_key=True),
    Column('fandom_id', ForeignKey('fandoms.id'), primary_key=True),
)

annnouncements_tags = Table(
    'annnouncements_tags',
    BaseModel.metadata,
    Column('annnouncement_id', ForeignKey('announcements.id'), primary_key=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True),
)

annnouncements_nsfw_fetishes = Table(
    'annnouncements_nsfw_fetishes',
    BaseModel.metadata,
    Column('annnouncement_id', ForeignKey('announcements.id'), primary_key=True),
    Column('nsfw_fetish_id', ForeignKey('nsfw_fetishes.id'), primary_key=True),
)

annnouncements_nsfw_taboo = Table(
    'annnouncements_nsfw_taboo',
    BaseModel.metadata,
    Column('annnouncement_id', ForeignKey('announcements.id'), primary_key=True),
    Column('nsfw_taboo_id', ForeignKey('nsfw_taboo.id'), primary_key=True),
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


class NsfwFetishModel(BaseModel):
    __tablename__ = 'nsfw_fetishes'

    name: Mapped[str] = mapped_column(String(256), unique=True, index=True)


class NsfwTabooModel(BaseModel):
    __tablename__ = 'nsfw_taboo'

    name: Mapped[str] = mapped_column(String(256), unique=True, index=True)


class FandomModel(BaseModel):
    __tablename__ = 'fandoms'

    name: Mapped[str] = mapped_column(String(256), unique=True, index=True)


class TagModel(BaseModel):
    __tablename__ = 'tags'

    name: Mapped[str] = mapped_column(String(256), unique=True, index=True)


class AnnouncementModel(BaseModel):
    __tablename__ = 'announcements'

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    orientation: Mapped[str] = mapped_column(String(8), nullable=True)
    gender: Mapped[str] = mapped_column(String(7), nullable=True)
    description: Mapped[str]
    # posters_urls: List[] (M2M)

    fandoms: Mapped[list[FandomModel]] = relationship(secondary=annnouncements_fandoms)
    tags: Mapped[list[TagModel]] = relationship(secondary=annnouncements_tags)

    is_crossgender: Mapped[bool] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    is_anonymously: Mapped[bool] = mapped_column(default=True)
    is_verify: Mapped[bool] = mapped_column(default=False)

    is_nsfw: Mapped[bool] = mapped_column(default=False)
    nsfw_fetishes: Mapped[list[NsfwFetishModel]] = relationship(secondary=annnouncements_nsfw_fetishes)
    nsfw_taboo: Mapped[list[NsfwTabooModel]] = relationship(secondary=annnouncements_nsfw_taboo)