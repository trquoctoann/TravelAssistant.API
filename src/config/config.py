import os
from typing import List, Dict, ClassVar
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Configs(BaseSettings):
    ENV: str = os.getenv("ENV", "dev")
    API: str = "/api"
    PROJECT_NAME: str = "ta-api"

    # Mappers
    ENV_DATABASE_MAPPER: Dict[str, str] = {
        "prod": "ta",
        "stage": "stage-ta",
        "dev": "dev-ta",
        "test": "test-ta",
    }
    DB_ENGINE_MAPPER: Dict[str, str] = {
        "postgresql": "postgresql",
        "mysql": "mysql+pymysql",
    }

    PROJECT_ROOT: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Date formats
    DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S"
    DATE_FORMAT: str = "%Y-%m-%d"

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    # Database
    DB: str = os.getenv("DB", "mysql")
    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "Toan972002")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "3306")
    DB_ENGINE: str = DB_ENGINE_MAPPER.get(DB, "mysql")

    DATABASE_URI_FORMAT: str = "{db_engine}://{user}:{password}@{host}:{port}/{database}"

    DATABASE_URI: ClassVar[str] = DATABASE_URI_FORMAT.format(
        db_engine=DB_ENGINE,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=ENV_DATABASE_MAPPER[ENV],
    )

    # Pagination
    PAGE: int = 1
    PAGE_SIZE: int = 20
    ORDERING: str = "-id"

    class Config:
        case_sensitive = True


class TestConfigs(Configs):
    ENV: str = "test"


# Instantiate configs
configs = Configs()

# Environment-based configurations
if configs.ENV == "prod":
    pass
elif configs.ENV == "stage":
    pass
elif configs.ENV == "test":
    setting = TestConfigs()
