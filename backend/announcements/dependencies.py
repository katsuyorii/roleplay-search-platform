from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.dependencies.database import get_session
from users.dependencies import get_current_user
from users.models import UserModel

from .services import AnnouncementsService
from .repositories import AnnouncementsRepository


def get_announcements_repository(session: AsyncSession = Depends(get_session)) -> AnnouncementsRepository:
    return AnnouncementsRepository(session)

def get_announcements_service(announcements_repository: AnnouncementsRepository = Depends(get_announcements_repository), current_user: UserModel = Depends(get_current_user)) -> AnnouncementsService:
    return AnnouncementsService(announcements_repository, current_user)