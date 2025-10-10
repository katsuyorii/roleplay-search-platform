from fastapi import Depends

from users.dependencies import get_users_repository
from users.repositories import UsersRepository
from announcements.dependencies import get_fandoms_repository, get_tags_repository, get_nsfw_fetishes_taboo_repository
from announcements.repositories import FandomsRepository, TagsRepository, NsfwFetishTabooRepository

from .services import AdminService


def get_admin_service(fandoms_repository: FandomsRepository = Depends(get_fandoms_repository), tags_repository: TagsRepository = Depends(get_tags_repository), nsfw_fetishes_taboo_repository: NsfwFetishTabooRepository = Depends(get_nsfw_fetishes_taboo_repository), users_repository: UsersRepository = Depends(get_users_repository)) -> AdminService:
    return AdminService(fandoms_repository, tags_repository, nsfw_fetishes_taboo_repository, users_repository)