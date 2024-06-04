from flask import Flask, request
from flask import send_from_directory
from flask_cors import CORS
import main
import os

app = Flask(__name__)
CORS(app)
PORT = 8080

PATH = "frontend"
VERSION = "v1"

@app.route('/')
def index():
    return send_from_directory(PATH, 'index.html')

@app.route('/<path:filename>')
def send_report(filename):
    return send_from_directory(PATH, filename)

@app.route(f'/{VERSION}/get-output', methods=['POST'])
def jql_query():
    ticket = request.json['ticket']
    return main.get_response_based_on_ticket(ticket)

@app.route(f'/{VERSION}/ask-question', methods=['POST'])
def chat():
    question = request.json['question']
    return main.get_response_from_question(question)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)