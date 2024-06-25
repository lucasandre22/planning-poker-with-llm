from dotenv import load_dotenv
import psycopg2
import json
from psycopg2 import sql
import os

load_dotenv()

db_params = {
    'dbname': os.environ['DB_NAME'],
    'user': os.environ['DB_USER'],
    'password': os.environ['DB_PASSWORD'],
    'host': 'localhost',
    'port': os.environ['DB_PORT']
}

# Establish the connection
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

SELECT_TICKET_QUERY = """
SELECT id, data->'content' AS ticket FROM tickets WHERE data->'content'->>'ticket' = '{ticket}'
"""

def get_ticket_from_database(ticket_query: str):
    cur.execute(SELECT_TICKET_QUERY.format(ticket=ticket_query.upper()))
    rows = cur.fetchall()
    return rows[0][1]