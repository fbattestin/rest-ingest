from pydantic import BaseModel, Field

class SchemaPayload(BaseModel):
    """
    Model defining the format of the schema payload to be registered.
    """
    schema_name: str = Field(..., description="Name of the schema")
    version: str = Field(..., description="Version of the schema")
    schema_definition: dict = Field(..., description="Definition of the schema")