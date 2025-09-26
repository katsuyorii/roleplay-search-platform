from fastapi import APIRouter, Depends, status, Request, Response

from src.limiter import limiter

from .services import AuthService
from .dependencies import get_auth_service
from .schemas import AccessTokenResponseSchema, UserCreatedResponse, UserRegistrationSchema, UserLoginSchema


auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth'],
)

@auth_router.post('/registration', response_model=UserCreatedResponse, status_code=status.HTTP_201_CREATED)
@limiter.limit('5/minute')
async def registration_user(user_data: UserRegistrationSchema, request: Request, auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.registration(user_data, request)

@auth_router.post('/login', response_model=AccessTokenResponseSchema)
@limiter.limit('10/minute')
async def login_user(user_data: UserLoginSchema, request: Request, response: Response, auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.authentication(user_data, response)