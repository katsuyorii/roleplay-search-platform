import uuid

from fastapi import APIRouter, Depends

from .dependencies import get_announcements_service
from .schemas import AnnouncementResponseSchema
from .services import AnnouncementsService


announcements_router = APIRouter(
    prefix='/announcements',
    tags=['Announcements'],
)

@announcements_router.get('', response_model=list[AnnouncementResponseSchema])
async def get_announcements(announcements_service: AnnouncementsService = Depends(get_announcements_service)):
    return await announcements_service.get_all()

@announcements_router.get('/{announcement_id}', response_model=AnnouncementResponseSchema)
async def get_announcement(announcement_id: uuid.UUID,announcements_service: AnnouncementsService = Depends(get_announcements_service)):
    return await announcements_service.get(announcement_id)