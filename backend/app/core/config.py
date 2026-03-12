from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str = "secret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    EMAIL_USER: str
    EMAIL_PASS: str

    model_config = {
        "env_file": ".env",
        "extra": "ignore"
    }


settings = Settings()
