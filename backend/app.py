from flask import Flask, request
from flask import send_from_directory
from flask_cors import CORS
from main import get_response_from_question, get_response_based_on_ticket
import os
import json

main = Flask(__name__)
CORS(main)
PORT = 8080

PATH = "../frontend"
VERSION = "v1"

@main.route('/')
def index():
    return send_from_directory(PATH, 'index.html')

@main.route('/<path:filename>')
def send_report(filename):
    return send_from_directory(PATH, filename)

@main.route(f'/{VERSION}/get-output', methods=['POST'])
def get_output():
    ticket = request.json['ticket']
    return get_response_based_on_ticket(ticket)

@main.route(f'/{VERSION}/ask-question', methods=['POST'])
def chat():
    question = request.json['question']
    # tentar pegar contexto do que foi retornado e tickets
    return get_response_from_question(question)

@main.route(f'/ticket_sample', methods=['POST'])
def ticket_sample():
    return {
        "recommended_story_points": "5",
        "result": "    Hello, I'm glad to provide you with my insights regarding the similar tickets and assist you with estimating your new ticket. Here are some key points:\n\n    Similarities: All four tickets involve bugs affecting the user interface or experience in one way or another. In particular, three of them deal specifically with the login page, while the other two pertain to user registration issues. Considering these similarities, it is likely that your team has a good understanding of the affected components and can estimate the new ticket accurately based on previous experiences.\n\n    Differences: While the first ticket involves a minor alignment issue, the other three tickets describe more significant problems that could have a wider impact on the application's functionality. Ticket #78 and #95 both address issues with user registration, but these are distinct issues requiring different solutions. Additionally, each ticket has a different priority level, which may affect your estimation process.\n\n    Important factors to consider:\n    1) Familiarity with the affected components (frontend react, backend node.js) and relevant experience in solving similar bugs.\n    2) The extent of the impact on the application's functionality or user experience. Ticket #78 and #95 involve issues that could potentially affect a larger number of users compared to the login page alignment issue.\n    3) Any additional factors specific to your new ticket that might influence its estimation, such as the urgency of fixing it or any known limitations in addressing similar bugs in the past.\n    4) The priority level and story points assigned to each ticket should also be considered. While story points are not always an accurate reflection of actual effort, they can provide a useful starting point for your estimation process.\n\n    Potential challenges:\n    1) The new ticket may require more extensive changes or involve complexities that were not present in the similar tickets. For instance, if the alignment issue extends beyond the login page, it could affect other pages and components as well.\n    2) Different browsers or operating systems might exhibit different behaviors with the application, complicating efforts to fix cross-browser compatibility issues (ticket #51).\n    3) User registration issues often require careful consideration of security implications and integration across multiple components. This could lead to longer estimation times as your team assesses potential risks and develops an appropriate solution.\n\n    Additional guidance:\n    1) Review the specific details in each ticket, including any notes or comments from previous development efforts.\n    2) Collaborate with other team members who were involved in resolving similar bugs to gather their perspectives and insights.\n    3) Consider using a ticketing tool with advanced estimation features that can provide additional data and insights based on the ticket's context.",
        "similar_tickets": [
            {
                "description": "There's a small alignment issue on the login page where the input fields are not properly aligned with the labels.",
                "summary": "Fix login page UI glitch",
                "ticket": "METHODS-1"
            },
            {
                "description": "Identify and fix issues causing discrepancies in the appearance or behavior of the application across different web browsers.",
                "summary": "Fix cross-browser compatibility issues",
                "ticket": "METHODS-51"
            },
            {
                "description": "Identify and fix issues with the user registration flow that prevent users from successfully creating accounts or encounter errors during registration.",
                "summary": "Fix broken user registration flow",
                "ticket": "METHODS-78"
            },
            {
                "description": "Identify and fix issues with the user registration flow that prevent users from successfully creating accounts or encounter errors during registration.",
                "summary": "Fix broken user registration flow",
                "ticket": "METHODS-95"
            }
        ]
    }

if __name__ == '__main__':
    main.run(host="0.0.0.0", port=PORT)

#fazer swagger api