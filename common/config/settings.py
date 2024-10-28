"""
Configuration settings for the application.
"""
import os

class Settings:
    """
    Defines configuration settings.
    """
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:8001")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    S3_BUCKET_NAME: str = os.getenv("S3_BUCKET_NAME", "my_bucket")
    AWS_REGION: str = os.getenv("AWS_REGION", "us-east-1")

settings = Settings()
