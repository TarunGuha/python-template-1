from pydantic import BaseSettings, Field


class DatabaseSettings(BaseSettings):
    database_name: str = Field(..., env="DATABASE_NAME")
    database_user: str = Field(..., env="DATABASE_USER")
    database_password: str = Field(..., env="DATABASE_PASSWORD")
    database_host: str = Field(..., env="DATABASE_HOST")
    database_port: str = Field(..., env="DATABASE_PORT")

    class Config:
        env_file = ".env"

    def get_connection_url(self) -> str:
        connection_url = "postgresql://{database_user}:{database_password}@{database_host}:{database_port}/{database_name}".format(
            database_user=self.database_user,
            database_password=self.database_password,
            database_host=self.database_host,
            database_port=self.database_port,
            database_name=self.database_name,
        )
        return connection_url
