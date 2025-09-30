from .models import UserModel
from .repositories import UsersRepository
from .schemas import UserUpdateSchema


class UsersService:
    def __init__(self, users_repository: UsersRepository, current_user: UserModel):
        self.users_repository = users_repository
        self.current_user = current_user
    
    async def get_current_user(self) -> UserModel:
        return self.current_user
    
    async def update_current_user(self, updated_user_data: UserUpdateSchema) -> UserModel:
        updated_user_data_dict = updated_user_data.model_dump(exclude_unset=True)

        await self.users_repository.update(self.current_user, updated_user_data_dict)

        return self.current_user