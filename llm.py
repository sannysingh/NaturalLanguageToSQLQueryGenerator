import os
import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

SYSTEM_PROMPT = """You are an expert MySQL query generator. Given a database schema and a user question in plain English, write ONE valid MySQL SELECT query that answers the question.

Rules:
- Only ever generate SELECT statements. Never write INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE, GRANT, or REVOKE.
- Use only the tables and columns provided in the schema below.
- Return Only the SQL query, wrapped in a '''sql code block. No explanation.
- If the question cannot be answered with the given schema, return: SELECT 'Cannot answer with available schema' AS error;
"""

def build_prompt(schema: str, question: str) -> str:
    return f"""Database schema:
{schema}

User question: {question}

Write the MySQL query."""

def extract_sql(text: str) -> str:
    """Pull the SQL out of a ```sql ...``` code block."""
    match = re.search(r"```sql\s*(.*?)```", text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return text.strip()

def is_safe_select(sql: str) -> bool:
    """Guardrail: only allow SELECT queries through to the database."""
    forbidden = ["insert", "update", "delete", "drop", "alter", "truncate", "create", "grant", "revoke"]
    lowered = sql.lower().strip()
    return lowered.startswith("select") and not any(word in lowered for word in forbidden)

def generate_sql(schema: str, question: str) -> str:
    """Call Groq to turn a plain-English question into SQL."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": build_prompt(schema, question)},],
        temperature=0,
        max_tokens=300,
    )
    raw = response.choices[0].message.content
    sql = extract_sql(raw)

    if not is_safe_select(sql):
        raise ValueError(f"Generated query failed the safety check:\n{sql}")

    return sql