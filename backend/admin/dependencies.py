from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.dependencies.database import get_session
from announcements.dependencies import get_fandoms_repository, get_tags_repository, get_nsfw_fetishes_taboo_repository
from announcements.repositories import FandomsRepository, TagsRepository, NsfwFetishTabooRepository

from .services import AdminService


def get_admin_service(session: AsyncSession = Depends(get_session), fandoms_repository: FandomsRepository = Depends(get_fandoms_repository), tags_repository: TagsRepository = Depends(get_tags_repository), nsfw_fetishes_taboo_repository: NsfwFetishTabooRepository = Depends(get_nsfw_fetishes_taboo_repository)) -> AdminService:
    return AdminService(fandoms_repository, tags_repository, nsfw_fetishes_taboo_repository, session)