from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.dependencies.database import get_session
from users.dependencies import get_current_user
from users.models import UserModel

from .services import AnnouncementsService
from .repositories import AnnouncementsRepository, FandomsRepository, TagsRepository, NsfwFetishTabooRepository


def get_fandoms_repository(session: AsyncSession = Depends(get_session)) -> FandomsRepository:
    return FandomsRepository(session)

def get_tags_repository(session: AsyncSession = Depends(get_session)) -> TagsRepository:
    return TagsRepository(session)

def get_nsfw_fetishes_taboo_repository(session: AsyncSession = Depends(get_session)) -> NsfwFetishTabooRepository:
    return NsfwFetishTabooRepository(session)

def get_announcements_repository(session: AsyncSession = Depends(get_session), fandoms_repository: FandomsRepository = Depends(get_fandoms_repository), tags_repository: TagsRepository = Depends(get_tags_repository), nsfw_fetishes_taboo_repository: NsfwFetishTabooRepository = Depends(get_nsfw_fetishes_taboo_repository)) -> AnnouncementsRepository:
    return AnnouncementsRepository(fandoms_repository, tags_repository, nsfw_fetishes_taboo_repository, session)

def get_announcements_service(announcements_repository: AnnouncementsRepository = Depends(get_announcements_repository), current_user: UserModel = Depends(get_current_user)) -> AnnouncementsService:
    return AnnouncementsService(announcements_repository, current_user)