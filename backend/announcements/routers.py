import uuid

from fastapi import APIRouter, Depends

from fastapi_filter import FilterDepends

from .dependencies import get_announcements_service
from .schemas import AnnouncementResponseSchema
from .services import AnnouncementsService
from .filters import AnnouncementFilter


announcements_router = APIRouter(
    prefix='/announcements',
    tags=['Announcements'],
)

@announcements_router.get('', response_model=list[AnnouncementResponseSchema])
async def get_announcements(announcements_filter: AnnouncementFilter = FilterDepends(AnnouncementFilter), announcements_service: AnnouncementsService = Depends(get_announcements_service)):
    return await announcements_service.get_all(announcements_filter)

@announcements_router.get('/{announcement_id}', response_model=AnnouncementResponseSchema)
async def get_announcement(announcement_id: uuid.UUID,announcements_service: AnnouncementsService = Depends(get_announcements_service)):
    return await announcements_service.get(announcement_id)