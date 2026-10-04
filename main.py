from dotenv import load_dotenv
from tabulate import tabulate
from db import get_connection, get_schema, run_query
from llm import generate_sql

load_dotenv()

def main():
    conn = get_connection()
    schema = get_schema(conn)

    print("Connected to MySQL. Schema loaded")
    print("Ask a question in plain English (or type 'exit' to quit).\n")

    while True:
        question = input("Ask> ").strip()
        if question.lower() in ("exit", "quit"):
            break
        if not question:
            continue

        try:
            sql = generate_sql(schema, question)
            print(f"\nGenerated SQL:\n {sql}\n")

            columns, rows = run_query(conn, sql)
            if rows is not None:
                print(tabulate(rows, headers=columns, tablefmt="grid"))
            else:
                print("Query executed successfully.")
        except Exception as e:
            print(f"Error: {e}")

        print()
    conn.close()
    print("Goodbye!")

if __name__ == "__main__":
    main()
    
