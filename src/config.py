"""Application configuration."""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings from environment variables."""
    
    # FastAPI Configuration
    FAST_API_HOST: str = "0.0.0.0"
    FAST_API_PORT: int = 8000
    FAST_API_RELOAD: bool = True
    FAST_API_WORKERS: int = 4
    
    # Database Configuration
    DATABASE_URL: str = "postgresql://automation_user:automation_password@localhost:5432/automation_db"
    DATABASE_ECHO: bool = False
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 10
    
    # GitHub API Configuration
    GITHUB_API_TOKEN: Optional[str] = None
    GITHUB_API_BASE_URL: str = "https://api.github.com"
    GITHUB_WEBHOOK_SECRET: Optional[str] = None
    
    # Qdrant Configuration
    QDRANT_URL: str = "http://localhost:6333"
    QDRANT_API_KEY: Optional[str] = None
    QDRANT_COLLECTION_NAME: str = "code_embeddings"
    QDRANT_VECTOR_SIZE: int = 1536
    
    # Event Stream Configuration
    EVENT_STREAM_ENABLED: bool = True
    EVENT_STREAM_BATCH_SIZE: int = 100
    EVENT_STREAM_TIMEOUT_SECONDS: int = 30
    
    # Logging Configuration
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"
    
    # Application Configuration
    APP_NAME: str = "Backend Automation Platform"
    APP_VERSION: str = "1.0.0"
    APP_ENV: str = "development"
    
    class Config:
        """Pydantic config."""
        env_file = ".env"
        case_sensitive = True


settings = Settings()
