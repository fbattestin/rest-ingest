"""
Endpoints for contract management in the API.
"""
from fastapi import APIRouter, Header, HTTPException
from models.contract import ContractPayload
from api.dependencies.validation import validate_contract
from common.utils import setup_logging, get_tracking_id,init_db
import sqlite3
import json
import os

DATABASE = os.getenv("DATABASE_URL", "contracts.db")

init_db()

logger = setup_logging()
router = APIRouter()

@router.post("/register", summary="Register New Contract", response_description="Contract registered successfully")
async def register_contract(
    payload: ContractPayload,
    # x_contract_name: str = Header(..., alias="X-Contract-Name"),
    # x_contract_version: str = Header(..., alias="X-Contract-Version")
) -> dict:
    """
    Endpoint to register a new contract in the Contract Registry.
    """
    logger.info(f"Registering contract: {payload.contract_name}, version: {payload.version}")
    # logger.info(f"Contract Name: {x_contract_name}, Contract Version: {x_contract_version}")
    idempotency_key = get_tracking_id()

    # Save contract to SQLite
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO contracts (contract_name, version, contract_details) VALUES (?, ?, ?)''',
            (payload.contract_name, payload.version, json.dumps(payload.contract_details))
        )
        conn.commit()
    logger.info("Contract registration process completed successfully")
    return {"message": "Contract registered successfully", "contract_name": payload.contract_name, "version": payload.version, "tracking_id": idempotency_key}

@router.get("/get/{contract_name}", summary="Get Contract", response_description="Contract details retrieved successfully")
async def get_contract(contract_name: str, version: str) -> dict:
    """
    Endpoint to retrieve a registered contract.
    """
    logger.info(f"Retrieving contract: {contract_name}, version: {version}")
    contract = await validate_contract(contract_name=contract_name, contract_version=version)

    return contract
    # with sqlite3.connect(DATABASE) as conn:
    #     cursor = conn.cursor()
    #     cursor.execute(
    #         '''SELECT contract_details FROM contracts WHERE contract_name = ? AND version = ?''',
    #         (contract_name, version)
    #     )
    #     row = cursor.fetchone()
    #     if row is None:
    #         logger.error(f"Contract with name {contract_name} and version {version} not found")
    #         raise HTTPException(status_code=404, detail="Contract not found")
    #     contract_details = json.loads(row[0])
    # logger.info("Contract retrieval process completed successfully")
    # return {"contract_name": contract_name, "version": version, "contract_details": contract_details}