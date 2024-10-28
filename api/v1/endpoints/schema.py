"""
Endpoints for schema management in the API.
"""
from fastapi import APIRouter, Header
from models.schema import SchemaPayload
from common.utils.logging import setup_logging
import uuid

logger = setup_logging()

router = APIRouter()


def get_idempotency_key() -> str:
    """
    Generates a unique key for idempotency control.
    """
    return str(uuid.uuid4())

@router.post("/register", summary="Register New Schema", response_description="Schema registered successfully")
async def register_schema(
    payload: SchemaPayload,
    x_contract_name: str = Header(..., alias="X-Contract-Name"),
    x_contract_version: str = Header(..., alias="X-Contract-Version")
) -> dict:
    """
    Endpoint to register a new schema in the Schema Registry.
    """
    logger.info(f"Registering schema: {payload.schema_name}, version: {payload.version}")
    logger.info(f"Contract Name: {x_contract_name}, Contract Version: {x_contract_version}")
    idempotency_key = get_idempotency_key()
    logger.info("Schema registration process completed successfully")
    return {"message": "Schema registered successfully", "schema_name": payload.schema_name, "version": payload.version, "tracking_id": idempotency_key}

@router.get("/get/{schema_name}", summary="Get Schema", response_description="Schema details retrieved successfully")
async def get_schema(schema_name: str, version: str) -> dict:
    """
    Endpoint to retrieve a registered schema.
    """
    logger.info(f"Retrieving schema: {schema_name}, version: {version}")
    schema_definition = {"example_field": "example_value"}
    logger.info("Schema retrieval process completed successfully")
    return {"schema_name": schema_name, "version": version, "schema_definition": schema_definition}