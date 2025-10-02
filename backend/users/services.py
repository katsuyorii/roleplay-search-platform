from fastapi import Response

from announcements.models import AnnouncementModel
from announcements.repositories import AnnouncementsRepository
from announcements.schemas import AnnouncementCreateSchema

from .models import UserModel
from .repositories import UsersRepository
from .schemas import UserUpdateSchema


class UsersService:
    def __init__(self, users_repository: UsersRepository, announcements_repository: AnnouncementsRepository, current_user: UserModel):
        self.users_repository = users_repository
        self.announcements_repository = announcements_repository
        self.current_user = current_user
    
    async def get_current_user(self) -> UserModel:
        return self.current_user
    
    async def update_current_user(self, updated_user_data: UserUpdateSchema) -> UserModel:
        updated_user_data_dict = updated_user_data.model_dump(exclude_unset=True)

        await self.users_repository.update(self.current_user, updated_user_data_dict)

        return self.current_user
    
    async def delete_current_user(self, response: Response) -> None:
        self.users_repository.delete(self.current_user)

        response.delete_cookie('refresh_token')
    
    async def get_announcements_user(self) -> list[AnnouncementModel]:
        announcements = await self.announcements_repository.get_by_user_id(self.current_user.id)

        return announcements
    
    async def create_announcements_user(self, announcement_data: AnnouncementCreateSchema) -> AnnouncementModel:
        announcement_data_dict = announcement_data.model_dump(exclude_unset=True)
        announcement_data_dict['user_id'] = self.current_user.id

        new_announcement = await self.announcements_repository.create(announcement_data_dict)

        return new_announcement