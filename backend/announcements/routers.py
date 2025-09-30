from fastapi import APIRouter


announcements_router = APIRouter(
    prefix='/announcements',
    tags=['Announcements'],
)