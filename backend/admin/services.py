from slugify import slugify

from announcements.models import FandomModel

from announcements.repositories import FandomsRepository, TagsRepository, NsfwFetishTabooRepository
from .schemas import FandomCreateSchema


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
