from pydantic import BaseSettings, Field


class RedisSettings(BaseSettings):
    redis_host: str = Field(..., env="REDIS_HOST")
    redis_port: str = Field(..., env="REDIS_PORT")
    redis_username: str = Field(..., env="REDIS_USERNAME")
    redis_password: str = Field(..., env="REDIS_PASSWORD")
    redis_database: int = Field(0, env="REDIS_DATABASE")

    class Config:
        env_file = ".env"

    def get_redis_url(self) -> str:
        return "rediss://{}:{}@{}:{}/{}".format(
            self.redis_username,
            self.redis_password,
            self.redis_host,
            self.redis_port,
            self.redis_database,
        )
