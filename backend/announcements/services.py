import uuid

from .models import AnnouncementModel
from .repositories import AnnouncementsRepository
from .exceptions import AnnouncementNotFound


class AnnouncementsService:
    def __init__(self, announcements_repository: AnnouncementsRepository):
        self.announcements_repository = announcements_repository
    
    async def get_all(self) -> list[AnnouncementModel]:
        announcements = await self.announcements_repository.get_all()

        return announcements
    
    async def get(self, announcement_id: uuid.UUID) -> AnnouncementModel | None:
        announcement = await self.announcements_repository.get(announcement_id)

        if announcement is None:
            raise AnnouncementNotFound()

        return announcement