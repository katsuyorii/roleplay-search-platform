import uuid

from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from core.repositories.database_base import DatabaseBaseRepository

from .models import AnnouncementModel, FandomModel, TagModel, NsfwFetishTabooModel
from .filters import AnnouncementFilter


class FandomsRepository(DatabaseBaseRepository):
    def __init__(self, session: AsyncSession, model: FandomModel = FandomModel):
        super().__init__(session, model)
    
    async def get_by_ids(self, ids: list[uuid.UUID]):
        result = await self.session.execute(select(self.model).where(self.model.id.in_(ids)))

        return result.scalars().all()


class TagsRepository(FandomsRepository):
    def __init__(self, session: AsyncSession, model: TagModel = TagModel):
        super().__init__(session, model)


class NsfwFetishTabooRepository(FandomsRepository):
    def __init__(self, session: AsyncSession, model: NsfwFetishTabooModel = NsfwFetishTabooModel):
        super().__init__(session, model)


class AnnouncementsRepository(DatabaseBaseRepository):
    def __init__(self, fandoms_repository: FandomsRepository, tags_repository: TagsRepository, nsfw_fetishes_taboo_repository: NsfwFetishTabooRepository, session: AsyncSession, model: AnnouncementModel = AnnouncementModel):
        super().__init__(session, model)
        self.fandoms_repository = fandoms_repository
        self.tags_repository = tags_repository
        self.nsfw_fetishes_taboo_repository = nsfw_fetishes_taboo_repository
    
    async def get_all(self, announcements_filter: AnnouncementFilter, skip: int = 0, limit: int = 5) -> list[AnnouncementModel]:
        query = select(self.model).options(selectinload(self.model.fandoms), selectinload(self.model.tags), selectinload(self.model.nsfw_fetishes), selectinload(self.model.nsfw_taboo)).where(self.model.is_verify == True, self.model.is_active == True)
    
        filtered_query = announcements_filter.filter(query)

        paginated_query = filtered_query.offset(skip).limit(limit)
        
        result = await self.session.execute(paginated_query)
        
        return result.scalars().all()
    
    async def get(self, id: uuid.UUID) -> AnnouncementModel | None:
        result = await self.session.execute(select(self.model).options(selectinload(self.model.fandoms), selectinload(self.model.tags), selectinload(self.model.nsfw_fetishes), selectinload(self.model.nsfw_taboo)).where(self.model.id == id, self.model.is_verify == True, self.model.is_active == True))

        return result.scalar_one_or_none()
    
    async def get_by_user_id(self, user_id: uuid.UUID, announcements_filter: AnnouncementFilter, skip: int = 0, limit: int = 5) -> list[AnnouncementModel]:
        query = select(self.model).options(selectinload(self.model.fandoms), selectinload(self.model.tags), selectinload(self.model.nsfw_fetishes), selectinload(self.model.nsfw_taboo)).where(self.model.user_id == user_id)

        filtered_query = announcements_filter.filter(query)

        paginated_query = filtered_query.offset(skip).limit(limit)

        result = await self.session.execute(paginated_query)

        return result.scalars().all()
    
    async def get_by_user_id_and_id(self, id: uuid.UUID, user_id: uuid.UUID) -> AnnouncementModel | None:
        result = await self.session.execute(select(self.model).options(selectinload(self.model.fandoms), selectinload(self.model.tags), selectinload(self.model.nsfw_fetishes), selectinload(self.model.nsfw_taboo)).where(self.model.id == id, self.model.user_id == user_id))

        return result.scalar_one_or_none()
    
    async def create(self, obj_dict: dict) -> AnnouncementModel:
        obj = self.model(**obj_dict)

        if obj.fandoms:
            selected_fandoms = await self.fandoms_repository.get_by_ids(obj_dict.get('fandoms'))
            obj.fandoms = selected_fandoms
        
        if obj.tags:
            selected_tags = await self.tags_repository.get_by_ids(obj_dict.get('tags'))
            obj.tags = selected_tags
        
        if obj.nsfw_fetishes:
            selected_nsfw_fetishes = await self.nsfw_fetishes_taboo_repository.get_by_ids(obj_dict.get('nsfw_fetishes'))
            obj.nsfw_fetishes = selected_nsfw_fetishes
        
        if obj.nsfw_taboo:
            selected_nsfw_taboo = await self.nsfw_fetishes_taboo_repository.get_by_ids(obj_dict.get('nsfw_taboo'))
            obj.nsfw_taboo = selected_nsfw_taboo

        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj, ['fandoms', 'tags', 'nsfw_fetishes', 'nsfw_taboo'])

        return obj
    
    async def update(self, obj: AnnouncementModel, updated_obj_dict: dict) -> AnnouncementModel:
        for key, value in updated_obj_dict.items():
            if key == 'fandoms':
                selected_fandoms = await self.fandoms_repository.get_by_ids(updated_obj_dict.get('fandoms'))
                value = selected_fandoms
            if key == 'tags':
                selected_tags = await self.tags_repository.get_by_ids(updated_obj_dict.get('tags'))
                value = selected_tags
            if key == 'nsfw_fetishes':
                selected_nsfw_fetishes = await self.nsfw_fetishes_taboo_repository.get_by_ids(updated_obj_dict.get('nsfw_fetishes'))
                value = selected_nsfw_fetishes
            if key == 'nsfw_taboo':
                selected_nsfw_taboo = await self.nsfw_fetishes_taboo_repository.get_by_ids(updated_obj_dict.get('nsfw_taboo'))
                value = selected_nsfw_taboo

            setattr(obj, key, value)

        await self.session.commit()
        await self.session.refresh(obj, ['fandoms', 'tags', 'nsfw_fetishes', 'nsfw_taboo'])

        return obj