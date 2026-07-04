from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

print("Loading settings.py...")


class Settings(BaseSettings):
    app_name: str
    app_version: str
    app_env: str
    debug: bool

    database_url: str

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


@lru_cache
def get_settings():
    print("Creating Settings...")
    s = Settings()
    print("Settings created successfully!")
    return s


settings = get_settings()

print("Done loading settings.py")