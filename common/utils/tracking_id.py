from uuid import uuid4

def get_tracking_id() -> str:
    """
    Generates a unique key for idempotency control.
    """
    return str(uuid4())

