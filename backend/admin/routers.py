from fastapi import APIRouter, Depends, status

from .dependencies import get_admin_service
from .services import AdminService
from .schemas import FandomResponseSchema, FandomCreateSchema


admin_router = APIRouter(
    prefix='/admin',
    tags=['Admin'],
)

@admin_router.get('/fandoms', response_model=list[FandomResponseSchema])
async def get_fandoms(admin_service: AdminService = Depends(get_admin_service), skip: int| None = None, limit: int | None = None):
    return await admin_service.get_fandoms_admin(skip, limit)

@admin_router.post('/fandoms', response_model=FandomResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_fandom(fandom_data: FandomCreateSchema, admin_service: AdminService = Depends(get_admin_service)):
    return await admin_service.create_fandom_admin(fandom_data)