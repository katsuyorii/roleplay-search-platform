import uuid

from .models import AnnouncementModel
from .repositories import AnnouncementsRepository
from .exceptions import AnnouncementNotFound
from .filters import AnnouncementFilter


class AnnouncementsService:
    def __init__(self, announcements_repository: AnnouncementsRepository):
        self.announcements_repository = announcements_repository
    
    async def get_all(self, announcements_filter: AnnouncementFilter, skip: int | None = None, limit: int | None = None) -> list[AnnouncementModel]:
        announcements = await self.announcements_repository.get_all(announcements_filter, skip, limit)

        return announcements
    
    async def get(self, announcement_id: uuid.UUID) -> AnnouncementModel | None:
        announcement = await self.announcements_repository.get(announcement_id)

        if announcement is None:
            raise AnnouncementNotFound()

        return announcement