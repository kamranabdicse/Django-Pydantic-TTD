from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, PostgresDsn, validator


class Settings(BaseSettings):
    DATABASE_URI: PostgresDsn

    class Config:
        env_file = ".env"


settings = Settings()
