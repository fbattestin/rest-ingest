# common/utils/db.py
import sqlite3
import os

DATABASE = os.getenv("DATABASE_URL", "contracts.db")

def get_db_connection():
    """
    Returns a connection to the SQLite database.
    """
    return sqlite3.connect(DATABASE)

def init_db():
    """
    Initializes the SQLite database with necessary tables.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contracts (
                contract_name TEXT,
                version TEXT,
                contract_details TEXT
            )
        ''')
        conn.commit()
