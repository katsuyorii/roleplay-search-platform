from fastapi import HTTPException, status


class FandomNotFound(HTTPException):
    def __init__(self, status_code = status.HTTP_404_NOT_FOUND, detail = 'Fandom not found', headers = None):
        super().__init__(status_code, detail, headers)