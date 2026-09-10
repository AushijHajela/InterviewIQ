from pydantic_settings import BaseSettings #type: ignore


class Settings(BaseSettings):
    app_name: str = "InterviewIQ API"
    app_version: str = "0.1.0"
    debug: bool = True

    class Config:
        env_file = ".env"


settings = Settings()