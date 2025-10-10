import uuid

from fastapi import APIRouter, Depends, status

from fastapi_filter import FilterDepends

from announcements.filters import AnnouncementFilter
from users.schemas import UserResponseSchema

from .dependencies import get_admin_service
from .services import AdminService
from .schemas import AnnouncementAdminResponseSchema, AnnouncementAdminUpdateSchema, FandomResponseSchema, FandomCreateSchema, FandomUpdateSchema, TagResponseSchema, TagCreateSchema, NsfwFetishesTabooResponseSchema, NsfwFetishesTabooCreateSchema


admin_router = APIRouter(
    prefix='/admin',
    tags=['Admin'],
)

@admin_router.get('/users', response_model=list[UserResponseSchema])
async def get_users(admin_service: AdminService = Depends(get_admin_service), skip: int| None = None, limit: int | None = None):
    return await admin_service.get_users_admin(skip, limit)

@admin_router.get('/announcements', response_model=list[AnnouncementAdminResponseSchema])
async def get_announcements(admin_service: AdminService = Depends(get_admin_service), announcements_filter: AnnouncementFilter = FilterDepends(AnnouncementFilter), skip: int| None = None, limit: int | None = None):
    return await admin_service.get_announcements_admin(announcements_filter, skip, limit)

@admin_router.get('/announcements/{announcement_id}', response_model=AnnouncementAdminResponseSchema)
async def get_announcement(announcement_id: uuid.UUID, admin_service: AdminService = Depends(get_admin_service)):
    return await admin_service.get_announcement_admin(announcement_id)

@admin_router.patch('/announcements/{announcement_id}', response_model=AnnouncementAdminResponseSchema)
async def update_announcement(announcement_id: uuid.UUID, updated_announcement_data: AnnouncementAdminUpdateSchema, admin_service: AdminService = Depends(get_admin_service)):
    return await admin_service.update_announcement_admin(announcement_id, updated_announcement_data)

@admin_router.delete('/announcements/{announcement_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_announcement(announcement_id: uuid.UUID, admin_service: AdminService = Depends(get_admin_service)):
    return await admin_service.delete_announcement_admin(announcement_id)

@admin_router.get('/fandoms', response_model=list[FandomResponseSchema])
async def get_fandoms(admin_service: AdminService = Depends(get_admin_service), skip: int| None = None, limit: int | None = None):
    return await admin_service.get_fandoms_admin(skip, limit)

@admin_router.get('/fandoms/{fandom_id}', response_model=FandomResponseSchema)
async def get_fandom(fandom_id: uuid.UUID, admin_service: AdminService = Depends(get_admin_service)):
    return await admin_service.get_fandom_admin(fandom_id)

@admin_router.post('/fandoms', response_model=FandomResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_fandom(fandom_data: FandomCreateSchema, admin_service: AdminService = Depends(get_admin_service)):
    return await admin_service.create_fandom_admin(fandom_data)

@admin_router.patch('/fandoms/{fandom_id}', response_model=FandomResponseSchema)
async def update_fandom(fandom_id: uuid.UUID, updated_fandom_data: FandomUpdateSchema, admin_service: AdminService = Depends(get_admin_service)):
    return await admin_service.update_fandom_admin(fandom_id, updated_fandom_data)

@admin_router.delete('/fandoms/{fandom_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_fandom(fandom_id: uuid.UUID, admin_service: AdminService = Depends(get_admin_service)):
    return await admin_service.delete_fandom_admin(fandom_id)

@admin_router.get('/tags', response_model=list[TagResponseSchema])
async def get_tags(admin_service: AdminService = Depends(get_admin_service), skip: int| None = None, limit: int | None = None):
    return await admin_service.get_tags_admin(skip, limit)

@admin_router.post('/tags', response_model=TagResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_tag(tag_data: TagCreateSchema, admin_service: AdminService = Depends(get_admin_service)):
    return await admin_service.create_tag_admin(tag_data)

@admin_router.get('/nsfw', response_model=list[NsfwFetishesTabooResponseSchema])
async def get_fetishes_taboo(admin_service: AdminService = Depends(get_admin_service), skip: int| None = None, limit: int | None = None):
    return await admin_service.get_nsfw_fetishes_taboo_admin(skip, limit)

@admin_router.post('/nsfw', response_model=NsfwFetishesTabooResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_fetish_taboo(nsfw_fetish_taboo_data: NsfwFetishesTabooCreateSchema, admin_service: AdminService = Depends(get_admin_service)):
    return await admin_service.create_nsfw_fetishes_taboo_admin(nsfw_fetish_taboo_data)