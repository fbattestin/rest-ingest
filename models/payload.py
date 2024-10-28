from pydantic import BaseModel, Field

class DataPayload(BaseModel):
    # source: str = Field(..., description="Identificação da fonte de dados")
    # timestamp: str = Field(..., description="Timestamp no formato ISO 8601")
    data: dict = Field(..., description="Dados do payload conforme contrato")



