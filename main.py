from api.v1.endpoints.data import data
from fastapi import FastAPI
from api.v1.endpoints import schema, contract, health
from common.utils import setup_logging, init_db

logger = setup_logging()

app = FastAPI(title="REST Ingest Data API", description="API for data ingestion, schema registration, and contract management.")

app.include_router(data.router, prefix="/api/v1/data", tags=["Data Ingest"])
app.include_router(schema.router, prefix="/api/v1/schema", tags=["Schema Management"])
app.include_router(contract.router, prefix="/api/v1/contract", tags=["Contract Management"])
app.include_router(health.router, prefix="/api/v1", tags=["Health Check"])

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting contracts database...")
    init_db()
    logger.info("Starting the server...")
    uvicorn.run("main:app", host="0.0.0.0", port=8000) #, reload=True, workers=4)