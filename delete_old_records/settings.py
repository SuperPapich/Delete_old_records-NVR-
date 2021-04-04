from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    erudite_url: str = Field(..., env="ERUDITE_URL")
    erudite_api_key: str = Field(..., env="ERUDITE_API_KEY")

    creds_path: str = Field(..., env="CREDS_PATH")
    token_path: str = Field(..., env="TOKEN_PATH")

    del_date: str = Field(..., env="DATE_TIME")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings(_env_file=".env")
