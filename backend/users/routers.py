from fastapi import APIRouter, Depends, Response, status

from announcements.schemas import AnnouncementResponseSchema, AnnouncementCreateSchema

from .dependencies import get_users_service
from .services import UsersService
from .schemas import UserResponseSchema, UserUpdateSchema


users_router = APIRouter(
    prefix='/users',
    tags=['Users'],
)

@users_router.get('/me', response_model=UserResponseSchema)
async def get_me(users_service: UsersService = Depends(get_users_service)):
    return await users_service.get_current_user()

@users_router.patch('/me', response_model=UserResponseSchema)
async def update_me(updated_user_data: UserUpdateSchema, users_service: UsersService = Depends(get_users_service)):
    return await users_service.update_current_user(updated_user_data)

@users_router.delete('/me', status_code=status.HTTP_204_NO_CONTENT)
async def delete_me(response: Response, users_service: UsersService = Depends(get_users_service)):
    return await users_service.delete_current_user(response)

@users_router.get('/me/announcements', response_model=list[AnnouncementResponseSchema])
async def get_announcements_me(users_service: UsersService = Depends(get_users_service)):
    return await users_service.get_announcements_user()

@users_router.post('/me/announcements', response_model=AnnouncementResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_announcement_me(announcement_data: AnnouncementCreateSchema, users_service: UsersService = Depends(get_users_service)):
    return await users_service.create_announcements_user(announcement_data)