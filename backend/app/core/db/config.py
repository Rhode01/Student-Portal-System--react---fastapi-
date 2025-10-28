from typing import Any, Union
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn, field_validator
from pathlib import Path
ENV_PATH =(Path(__file__).resolve().parents[4] / ".env")
class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str = "5432"

    AUTH0_DOMAIN: str 
    AUTH0_CLIENT_ID: str 
    AUTH0_CLIENT_SECRET: str 
    AUTH0_API_AUDIENCE: str 
    
    SQLALCHEMY_DATABASE_URI: Union[PostgresDsn, None] = None

    model_config = SettingsConfigDict(env_file=ENV_PATH)
    @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    def assemble_db_connection(cls, v: str | None, values: dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=values.data.get("POSTGRES_USER"),
            password=values.data.get("POSTGRES_PASSWORD"),
            host=values.data.get("POSTGRES_HOST"),
            port=int(values.data.get("POSTGRES_PORT", 5432)),
            path=values.data.get('POSTGRES_DB'),  
        )

settings = Settings()