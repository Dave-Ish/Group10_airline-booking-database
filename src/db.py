"""MySQL connection helper. Settings come from environment variables."""
import os

import mysql.connector


def get_connection():
    """Return a new connection to airline_db. The password is never in source code."""
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        port=int(os.environ.get("DB_PORT", "3306")),
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ.get("DB_NAME", "airline_db"),
    )
