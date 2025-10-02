from fastapi import HTTPException, status


class AnnouncementNotFound(HTTPException):
    def __init__(self, status_code = status.HTTP_404_NOT_FOUND, detail = 'Announcement not found', headers = None):
        super().__init__(status_code, detail, headers)