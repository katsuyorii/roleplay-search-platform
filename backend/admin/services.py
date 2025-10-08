from announcements.repositories import FandomsRepository, TagsRepository, NsfwFetishTabooRepository


class AdminService:
    def __init__(self, fandoms_repository: FandomsRepository, tags_repository: TagsRepository, nsfw_fetishes_taboo_repository: NsfwFetishTabooRepository):
        self.fandoms_repository = fandoms_repository
        self.tags_repository = tags_repository
        self.nsfw_fetishes_taboo_repository = nsfw_fetishes_taboo_repository