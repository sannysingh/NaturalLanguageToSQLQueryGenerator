import os
import mysql.connector

def get_connection():
    """Open a connection to MySQL using credentials from .env """
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "company_db"),
        use_pure=True,
    )

def get_schema(conn):
    """Read all tables and their columns, formatted as text for the LLM prompt"""
    cursor=conn.cursor()
    cursor.execute("SHOW TABLES")
    tables= [row[0] for row in cursor.fetchall()]

    schema_parts = []
    for table in tables:
        cursor.execute(f"DESCRIBE {table}")
        columns = cursor.fetchall()
        col_lines = [f" - {col[0]} ({col[1]})" for col in columns]
        schema_parts.append(f"Table: {table}\n" + "\n".join(col_lines))
    cursor.close()
    return "\n\n".join(schema_parts)

def run_query(conn, sql):
    """Execute a SQL query and return (columns, rows) for SELECTs"""
    cursor = conn.cursor()
    cursor.execute(sql)

    if sql.strip().lower().startswith("select"):
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        cursor.close()
        return columns, rows

    conn.commmit()
    cursor.close()
    return None, None