from flask import Flask, request
from flask import send_from_directory
from flask_cors import CORS
from main import get_response_from_question, get_response_based_on_ticket
import os
import json

main = Flask(__name__)
CORS(main)
PORT = 8080

PATH = "frontend"
VERSION = "v1"

@main.route('/')
def index():
    return send_from_directory(PATH, 'index.html')

@main.route('/<path:filename>')
def send_report(filename):
    return send_from_directory(PATH, filename)

@main.route(f'/{VERSION}/get-output', methods=['POST'])
def jql_query():
    ticket = request.json['content']
    return get_response_based_on_ticket(ticket)

@main.route(f'/{VERSION}/ask-question', methods=['POST'])
def chat():
    question = request.json['question']
    return get_response_from_question(question)

if __name__ == '__main__':
    main.run(host="0.0.0.0", port=PORT)