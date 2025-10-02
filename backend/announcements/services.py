import uuid

from users.models import UserModel

from .models import AnnouncementModel
from .repositories import AnnouncementsRepository
from .schemas import AnnouncementCreateSchema
from .exceptions import AnnouncementNotFound


class AnnouncementsService:
    def __init__(self, announcements_repository: AnnouncementsRepository, current_user: UserModel):
        self.announcements_repository = announcements_repository
        self.current_user = current_user
    
    async def get_all(self) -> list[AnnouncementModel]:
        announcements = await self.announcements_repository.get_all()

        return announcements
    
    async def get(self, announcement_id: uuid.UUID) -> AnnouncementModel | None:
        announcement = await self.announcements_repository.get(announcement_id)

        if announcement is None:
            raise AnnouncementNotFound()

        return announcement
    
    async def create(self, announcement_data: AnnouncementCreateSchema) -> AnnouncementModel:
        announcement_data_dict = announcement_data.model_dump(exclude_unset=True)
        announcement_data_dict['user_id'] = self.current_user.id

        new_announcement = await self.announcements_repository.create(announcement_data_dict)

        return new_announcement