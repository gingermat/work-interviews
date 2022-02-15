import os


class Settings:
    DEBUG: bool = bool(os.getenv("DEBUG", False))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO") if not DEBUG else "DEBUG"

    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8080"))

    MONGODB_URL: str = os.getenv("MONGODB_URL", "mongodb://test_user:test_password@mongo:27017/test?maxpoolsize=5")

    INVENTORY_COLLECTION_NAME: str = os.getenv("INVENTORY_COLLECTION_NAME", "inventory")
    INVENTORY_ITEMS_PER_PAGE: int = int(os.getenv("INVENTORY_ITEMS_PER_PAGE", 50))


settings = Settings()
