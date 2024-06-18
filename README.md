# Planning Poker with AI Assistant

## Overview
Planning Poker with AI Assistant is a tool designed to assist software development teams in estimating the effort required for various tasks. The system leverages AI to provide context and guidance based on similar past tickets, improving the accuracy and efficiency of the estimation process.

## Features
- **Ticket Management**: Create, store, and manage project tickets.
- **Vectorization**: Convert ticket descriptions into vector representations for similarity search.
- **Similarity Search**: Find the top 3 most similar tickets using vector similarity.
- **AI Contextual Assistance**: Generate context and guidance based on similar tickets using an AI model.
- **Planning Poker Integration**: Integrate AI-generated insights into the planning poker workflow.
- **Feedback Loop**: Collect feedback on AI suggestions and continuously improve the model.

## Architecture
The project consists of the following components:

1. **Frontend**: User interface for creating tickets, viewing similar tickets, and displaying AI-generated context along with conversational chat.
2. **Backend**: API server for handling requests, integrating with the vector database, and interacting with the AI model.
3. **Vector Database**: Stores vectorized representations of tickets for similarity search. Implemented with FAISS.
4. **AI Model**: Generates context and guidance based on similar tickets. Uses mistrallite.

## Getting Started

### Prerequisites
- Python
- Ollama
- NVIDEA graphics card with at least 4 GB VRAM

### Installation

1. **Clone the Repository**
    ```sh
    git clone https://github.com/your-username/planning-poker-with-llm.git
    cd planning-poker-with-llm
    ```

2. **Install Backend Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. **Start the Backend Server**
    ```sh
    python ./app.py
    ```

The application should now be running on `http://localhost:5000`.

## Usage

1. **Ticket search**: Enter the ticket id that is currently being estimated and submit it.
2. **Vectorization and Similarity Search**: The system preprocesses and vectorizes the ticket description, then searches for the top 3 similar tickets and retrieve them as cards.
3. **AI Contextual Assistance**: The AI model analyzes the similar tickets and generates context and guidance to estimate the new ticket.
4. **Planning Poker Session**: The AI-generated insights are displayed during the planning poker session to assist the team in estimating the ticket.
