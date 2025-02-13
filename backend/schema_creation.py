import mysql.connector
import os
from db import get_db_connection

# Database connection
conn = get_db_connection()
cursor = conn.cursor()


# Read and execute the SQL file
with open("database/schema.sql", "r") as file:
    sql_statements = file.read()
    for statement in sql_statements.split(";"):
        statement = statement.strip()
        if statement:
            cursor.execute(statement)

with open("database/sample_data.sql", "r") as file:
    sql_statements = file.read()
    for statement in sql_statements.split(";"):
        statement = statement.strip()
        if statement:
            cursor.execute(statement)

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

print("Schema and sample data inserted successfully.")
