from flask import Flask, request
from flask import send_from_directory
from flask_cors import CORS
import os
from main import search_for_similar_tickets, get_response_based_on_ticket

app = Flask(__name__)
CORS(app)
PORT = 8001

PATH = "../frontend"

@app.route('/')
def index():
    return send_from_directory(PATH, 'index.html')

@app.route('/similarity_search', methods=['POST'])
def search_database():
    query = request.json['query']
    response = search_for_similar_tickets(query)
    return {response}

@app.route('/get_response', methods=['POST'])
def get_response_based():
    ticket = request.json['ticket']
    response = get_response_based_on_ticket(str(ticket))
    return { "response": response }


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)