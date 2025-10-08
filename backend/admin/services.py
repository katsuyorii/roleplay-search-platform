from slugify import slugify

from announcements.models import FandomModel, TagModel

from announcements.repositories import FandomsRepository, TagsRepository, NsfwFetishTabooRepository
from .schemas import FandomCreateSchema, TagCreateSchema


class AdminService:
    def __init__(self, fandoms_repository: FandomsRepository, tags_repository: TagsRepository, nsfw_fetishes_taboo_repository: NsfwFetishTabooRepository):
        self.fandoms_repository = fandoms_repository
        self.tags_repository = tags_repository
        self.nsfw_fetishes_taboo_repository = nsfw_fetishes_taboo_repository
    
    async def get_fandoms_admin(self, skip: int | None = None, limit: int | None = None) -> list[FandomModel]:
        fandoms = await self.fandoms_repository.get_all(skip, limit)

        return fandoms
    
    async def create_fandom_admin(self, fandom_data: FandomCreateSchema) -> FandomModel:
        fandom_data_dict = fandom_data.model_dump(exclude_unset=True)
        fandom_data_dict['slug'] = slugify(fandom_data.name)

        new_fandom = await self.fandoms_repository.create(fandom_data_dict)

        return new_fandom
    
    async def get_tags_admin(self, skip: int | None = None, limit: int | None = None) -> list[TagModel]:
        tags = await self.tags_repository.get_all(skip, limit)

        return tags
    
    async def create_tag_admin(self, tag_data: TagCreateSchema) -> TagModel:
        tag_data_dict = tag_data.model_dump(exclude_unset=True)
        tag_data_dict['slug'] = slugify(tag_data.name)

        new_tag = await self.tags_repository.create(tag_data_dict)

        return new_tag
