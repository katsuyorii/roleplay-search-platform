import uuid

from slugify import slugify

from users.models import UserModel
from users.repositories import UsersRepository
from announcements.repositories import AnnouncementsRepository
from announcements.models import FandomModel, TagModel, NsfwFetishTabooModel, AnnouncementModel
from announcements.filters import AnnouncementFilter

from announcements.repositories import FandomsRepository, TagsRepository, NsfwFetishTabooRepository
from .schemas import FandomCreateSchema, FandomUpdateSchema, TagCreateSchema, NsfwFetishesTabooCreateSchema
from .exceptions import FandomNotFound


class AdminService:
    def __init__(self, fandoms_repository: FandomsRepository, tags_repository: TagsRepository, nsfw_fetishes_taboo_repository: NsfwFetishTabooRepository, users_repository: UsersRepository, announcements_repository: AnnouncementsRepository):
        self.users_repository = users_repository
        self.fandoms_repository = fandoms_repository
        self.tags_repository = tags_repository
        self.nsfw_fetishes_taboo_repository = nsfw_fetishes_taboo_repository
        self.announcements_repository = announcements_repository
    
    async def get_users_admin(self, skip: int | None = None, limit: int | None = None) -> list[UserModel]:
        users = await self.users_repository.get_all(skip, limit)

        return users
    
    async def get_announcements_admin(self, announcements_filter: AnnouncementFilter, skip: int | None = None, limit: int | None = None) -> list[AnnouncementModel]:
        announcements = await self.announcements_repository.get_all(announcements_filter, skip, limit)

        return announcements
    
    async def get_fandoms_admin(self, skip: int | None = None, limit: int | None = None) -> list[FandomModel]:
        fandoms = await self.fandoms_repository.get_all(skip, limit)

        return fandoms
    
    async def get_fandom_admin(self, fandom_id: uuid.UUID) -> FandomModel:
        fandom = await self.fandoms_repository.get(fandom_id)

        if fandom is None:
            raise FandomNotFound()
        
        return fandom
    
    async def create_fandom_admin(self, fandom_data: FandomCreateSchema) -> FandomModel:
        fandom_data_dict = fandom_data.model_dump(exclude_unset=True)
        fandom_data_dict['slug'] = slugify(fandom_data.name)

        new_fandom = await self.fandoms_repository.create(fandom_data_dict)

        return new_fandom
    
    async def update_fandom_admin(self, fandom_id: uuid.UUID, updated_fandom_data: FandomUpdateSchema) -> FandomModel:
        updated_fandom_data_dict = updated_fandom_data.model_dump(exclude_unset=True)
        updated_fandom_data_dict['slug'] = slugify(updated_fandom_data.name)

        fandom = await self.fandoms_repository.get(fandom_id)

        if fandom is None:
            raise FandomNotFound()
        
        return await self.fandoms_repository.update(fandom, updated_fandom_data_dict)
    
    async def delete_fandom_admin(self, fandom_id: uuid.UUID) -> None:
        fandom = await self.fandoms_repository.get(fandom_id)

        if fandom is None:
            raise FandomNotFound()

        await self.fandoms_repository.delete(fandom)
    
    async def get_tags_admin(self, skip: int | None = None, limit: int | None = None) -> list[TagModel]:
        tags = await self.tags_repository.get_all(skip, limit)

        return tags
    
    async def create_tag_admin(self, tag_data: TagCreateSchema) -> TagModel:
        tag_data_dict = tag_data.model_dump(exclude_unset=True)
        tag_data_dict['slug'] = slugify(tag_data.name)

        new_tag = await self.tags_repository.create(tag_data_dict)

        return new_tag

    async def get_nsfw_fetishes_taboo_admin(self, skip: int | None = None, limit: int | None = None) -> list[NsfwFetishTabooModel]:
        tags = await self.nsfw_fetishes_taboo_repository.get_all(skip, limit)

        return tags
    
    async def create_nsfw_fetishes_taboo_admin(self, nsfw_fetish_taboo_data: NsfwFetishesTabooCreateSchema) -> NsfwFetishTabooModel:
        nsfw_fetish_taboo_data_dict = nsfw_fetish_taboo_data.model_dump(exclude_unset=True)
        nsfw_fetish_taboo_data_dict['slug'] = slugify(nsfw_fetish_taboo_data.name)

        new_nsfw_fetish_taboo = await self.nsfw_fetishes_taboo_repository.create(nsfw_fetish_taboo_data_dict)

        return new_nsfw_fetish_taboo
