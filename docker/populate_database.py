import psycopg2
import json
from psycopg2 import sql

JSONL_FILE_LOCATION="./backend/documents/tickets.jsonl"

# Database connection parameters
db_params = {
    'dbname': 'planning-poker',
    'user': 'postgres',
    'password': 'example',
    'host': 'localhost',
    'port': '5432'
}

# Establish the connection
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

# Drop the table if it exists
cur.execute("DROP TABLE IF EXISTS tickets")

# Create the table
create_table_query = """
CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    data JSONB
);
"""
cur.execute(create_table_query)
print("Table created successfully")

def insert_data(json_data):
    insert_query = "INSERT INTO tickets (data) VALUES (%s)"
    cur.execute(insert_query, (json_data,))

with open(JSONL_FILE_LOCATION, 'r') as file:
    for line in file:
        ticket = json.loads(line.strip())
        insert_data(json.dumps(ticket))
    print("Inserted all values from file ", JSONL_FILE_LOCATION, "to the database")

# Commit the transaction
conn.commit()
        
# Query data from the table
select_query = """
SELECT id, data->'content' AS ticket FROM tickets WHERE data->'content'->>'ticket' = 'METHODS-1'
"""
cur.execute(select_query)
rows = cur.fetchall()

## Print the queried data
for row in rows:
    print(f"id: {row[0]}, name: {row[1]}, age: {row[2]}, city: {row[3]}")

# Close the cursor and the connection
cur.close()
conn.close()
