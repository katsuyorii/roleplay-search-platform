from sqlalchemy.ext.asyncio import AsyncSession

from core.repositories.database_base import DatabaseBaseRepository

from .models import AnnouncementModel


class AnnouncementsRepository(DatabaseBaseRepository):
    def __init__(self, session: AsyncSession, model: AnnouncementModel = AnnouncementModel):
        super().__init__(session, model)

    async def create(self, obj_dict: dict) -> AnnouncementModel:
        obj = self.model(**obj_dict)

        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj, ['fandoms', 'tags', 'nsfw_fetishes', 'nsfw_taboo'])

        return obj
    