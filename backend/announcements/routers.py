from fastapi import APIRouter, Depends, status

from .dependencies import get_announcements_service
from .schemas import AnnouncementResponseSchema, AnnouncementCreateSchema
from .services import AnnouncementsService


announcements_router = APIRouter(
    prefix='/announcements',
    tags=['Announcements'],
)

@announcements_router.post('', response_model=AnnouncementResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_announcement(announcement_data: AnnouncementCreateSchema, announcements_service: AnnouncementsService = Depends(get_announcements_service)):
    return await announcements_service.create(announcement_data)