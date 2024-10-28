"""
Endpoints for data ingestion in the API.
"""
from fastapi import APIRouter, HTTPException, Header, Depends
from models.payload import DataPayload
from .contract import get_contract
from api.dependencies.redis import get_redis
from api.dependencies.validation import validate_contract
from common.utils import setup_logging, get_tracking_id
from common.services.s3_service import upload_to_s3


logger = setup_logging()

router = APIRouter()


@router.post("/ingest", summary="Data Ingestion", response_description="Ingestion confirmation")
async def ingest_data(
    payload: DataPayload,
    x_contract_name: str = Header(..., alias="X-Contract-Name"),
    x_contract_version: str = Header(..., alias="X-Contract-Version"),
    # redis=Depends(get_redis)
) -> dict:
    """
    Endpoint for data ingestion.
    Validates headers and payload, then stores the information in Redis or S3.
    """
    logger.info("Starting data ingestion process")
    logger.info(f"Received payload: {payload}")
    logger.info(f"Contract Name: {x_contract_name}, Contract Version: {x_contract_version}")

    contract = await validate_contract(x_contract_name, x_contract_version)
    logger.info(f"Contract: {contract}")

    idempotency_key = get_tracking_id()
    # await redis.set(idempotency_key, str(payload.dict()), ex=3600)
    logger.info(f"Data stored in Redis with idempotency key: {idempotency_key}")

    # factory calls here
    destination = contract["contract_details"]["dest"]
    logger.info(f"Contract Destination: {destination}")
    if destination == "queue":
        logger.info("Data will be sent to queue")
        pass
    elif destination == "cold_storage":
        logger.info("Data will be sent to cold storage")
        upload_to_s3(file_name=f"payload_{idempotency_key}.json", data=str(payload.dict()).encode())
    elif destination == "s3":
        logger.info(f"Data will be sent to S3://..../....")
    elif destination == "local":
        logger.info(f"Saving file local: {idempotency_key}.json")
        logger.info("Data ingestion process completed successfully")
        return {"status": "success", "tracking_id": idempotency_key}
    else:
        raise NotImplementedError("Ingest method not implemented yet.")

@router.get("/status/{data_id}", summary="Get Data Status", response_description="Status of ingested data")
async def get_data_status(data_id: str, redis=Depends(get_redis)) -> dict:
    """
    Endpoint to retrieve the status of ingested data.
    """
    logger.info(f"Retrieving status for data ID: {data_id}")
    status = await redis.get(data_id)
    if not status:
        logger.error(f"Data with ID {data_id} not found")
        raise HTTPException(status_code=404, detail="Data not found")
    logger.info(f"Data status retrieved successfully for ID {data_id}")
    return {"status": status.decode("utf-8")}