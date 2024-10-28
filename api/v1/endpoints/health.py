"""
Endpoint de verificação da saúde da API.
"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from common.utils.logging import setup_logging

logger = setup_logging()

router = APIRouter()

@router.get("/health", summary="Health Check", response_description="Application health status")
async def health_check() -> JSONResponse:
    """
    Endpoint to check the health of the application.
    Returns status 'ok' if everything is functioning properly.
    """
    logger.info("Performing health check")
    return JSONResponse(status_code=200, content={"status": "ok", "message": "The system is healthy"})
