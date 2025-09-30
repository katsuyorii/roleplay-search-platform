from sqlalchemy.ext.asyncio import AsyncSession

from core.repositories.database_base import DatabaseBaseRepository

from .models import AnnouncementModel


class AnnouncementsRepository(DatabaseBaseRepository):
    def __init__(self, session: AsyncSession, model: AnnouncementModel = AnnouncementModel):
        super().__init__(session, model)