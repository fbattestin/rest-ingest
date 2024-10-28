"""
Dependency for contract validation.
"""
from fastapi import HTTPException
from common.utils.logging import setup_logging
import sqlite3
import json
import os

logger = setup_logging()

DATABASE = os.getenv("DATABASE_URL", "contracts.db")

async def validate_contract(contract_name: str, contract_version: str):
    """
    Validates contract headers.
    """
    logger.info(f"Validating contract: {contract_name}, version: {contract_version}")
    if not contract_name or not contract_version:
        logger.error("Contract validation failed: missing name or version")
        raise HTTPException(status_code=400, detail="Invalid contract")
    logger.info("Contract validation successful")

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''SELECT contract_details FROM contracts WHERE contract_name = ? AND version = ?''',
            (contract_name, contract_version)
        )
        row = cursor.fetchone()
        if row is None:
            logger.error(f"Contract with name {contract_name} and version {contract_version} not found")
            raise HTTPException(status_code=404, detail="Contract not found")
        contract_details = json.loads(row[0])
    logger.info("Contract retrieval process completed successfully")
    return {"contract_name": contract_name, "version": contract_version, "contract_details": contract_details}