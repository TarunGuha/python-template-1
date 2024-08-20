from pydantic import BaseSettings, Field


class RedisSettings(BaseSettings):
    redis_host: str = Field(..., env="REDIS_HOST")
    redis_port: str = Field(..., env="REDIS_PORT")
    redis_username: str = Field(..., env="REDIS_USERNAME")
    redis_password: str = Field(..., env="REDIS_PASSWORD")
    redis_database: int = Field(0, env="REDIS_DATABASE")  # Default to 0 if not set

    class Config:
        env_file = ".env"

    def get_redis_url(self) -> str:
        return "rediss://{username}:{password}@{host}:{port}/{database}".format(
            username=self.redis_username,
            password=self.redis_password,
            host=self.redis_host,
            port=self.redis_port,
            database=self.redis_database,
        )
