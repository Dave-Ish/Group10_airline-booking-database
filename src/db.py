"""MySQL connection helper. Settings come from environment variables."""
import os

import mysql.connector


def get_connection():
    """Return a new connection to airline_db. The password is never in source code."""
    return mysql.connector.connect(
        host= "mysql-2b82013f-alustudent-010f.f.aivencloud.com",
        port=23310,
        user="avnadmin",
        password=os.environ["DB_PASSWORD"],

    )
