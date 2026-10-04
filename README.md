# Natural Language to SQL Query Generator

Ask questions about a MySQL database in plain English and get back real query results - powered by Groq's free LLM API

## Stack
Python, Groq API (LLaMA 3.3 70B), MySQL

## Setup
1. Clone the repo and create a virtual environment
2. 'pip install -r requorements.txt'
3. Load 'database/setup.sql' into MySQL
4. Copy '.env.eample' to '.env' and fill in your Groq API key + MySQL credentials
5. 'python main.py'

## Example
Ask> Who are the top 3 highest-paid employees in Engineering?
-> Generates and runs a SQL query, returns a formatted table.

## Safety
Only SELECT queries are permitted, enforced both in the prompt and in application code, so the LLM can never modify or delete data.