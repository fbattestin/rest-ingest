"""
Service module for handling interactions with Amazon S3.
"""
import boto3
from botocore.exceptions import NoCredentialsError
from common.utils.logging import setup_logging
from common.config.settings import settings

logger = setup_logging()

def upload_to_s3(file_name: str, data: bytes) -> bool:
    """
    Uploads data to an S3 bucket.
    """
    s3 = boto3.client('s3', region_name=settings.AWS_REGION)
    try:
        s3.put_object(Bucket=settings.S3_BUCKET_NAME, Key=file_name, Body=data)
        logger.info(f"Successfully uploaded {file_name} to S3 bucket {settings.S3_BUCKET_NAME}")
        return True
    except NoCredentialsError:
        logger.error("Credentials not available for S3 upload.")
        return False