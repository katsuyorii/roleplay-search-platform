from pydantic_settings import BaseSettings, SettingsConfigDict


class CustomBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='../.env', extra='allow')


class DatabaseSettings(CustomBaseSettings):
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int

    @property
    def DATABASE_URL(self) -> str:
        return f'postgresql+asyncpg://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


class RedisSettings(CustomBaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str


class JWTSettings(CustomBaseSettings):
    JWT_PUBLIC_KEY: str
    JWT_PRIVATE_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_MINUTES_EXPIRES: int
    JWT_REFRESH_TOKEN_DAYS_EXPIRES: int


database_settings = DatabaseSettings()
redis_settings = RedisSettings()
jwt_settings = JWTSettings()