from pydantic import BaseModel, Field

class ContractPayload(BaseModel):
    """
    Model defining the format of the contract payload to be registered.
    """
    contract_name: str = Field(..., description="Name of the contract")
    version: str = Field(..., description="Version of the contract")
    contract_details: dict = Field(..., description="Details of the contract")