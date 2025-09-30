from users.models import UserModel

from .repositories import AnnouncementsRepository


class AnnouncementsService:
    def __init__(self, announcements_repository: AnnouncementsRepository, current_user: UserModel):
        self.announcements_repository = announcements_repository
        self.current_user = current_user