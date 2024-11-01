import json
import logging
from jsonschema import validate, ValidationError

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

with open('schema.json', 'r') as schema_file:
    schema = json.load(schema_file)

def validate_contract(contract_str):
    try:
        contract = json.loads(contract_str)
        validate(instance=contract, schema=schema)
        logger.info("Contract is valid.")
        return True
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON format: {e}")
        return False
    except ValidationError as e:
        logger.error(f"Contract validation error: {e.message}")
        return False