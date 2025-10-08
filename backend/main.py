from fastapi import FastAPI

from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from src.limiter import limiter
from auth.routers import auth_router
from users.routers import users_router
from announcements.routers import announcements_router
from admin.routers import admin_router


app = FastAPI()

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(announcements_router)
app.include_router(admin_router)