
from vectorstore import search_for_similar_tickets
from ticket_handling import build_ticket_text, build_ticket_text_from_list
from llm import CHAIN, CHAIN_SIMILARITY, llm
from postgres import get_ticket_from_database
from llm_with_chat_history import LLMWithChatHistory
import time
import json

first_time_running = True
question_answering_chain = None
context_for_question_answering = {}

def context_definer(data_retrieved_from_similarity_search):
    print("Giving context to llm...")

def get_story_points_average_from_tickets(tickets):
    context = 0
    for ticket in tickets:
        context += ticket["story_points"]
    return context/len(tickets)

def get_closest_fibonacci_number(number):
    first = 0
    second = 1
    
    sum = first + second
    if number <= sum:
        return sum
    
    while sum <= number:
        first = second
        second = sum
        sum = first + second

    return sum

def init_ai_chat_conversation(new_ticket, similar_tickets, ai_response):
    global question_answering_chain
    question_answering_chain = LLMWithChatHistory(llm, new_ticket, similar_tickets, ai_response)

def get_response_based_on_ticket(ticket: str) -> dict:
    """_summary_
    Args:
        ticket (str): the ticket to search for similarity
    Returns:
        dict: JSON object containing result and recommended_story_points
    """
    global first_time_running
    global context_for_question_answering
    print("\nGetting ticket from database")
    ticket_response = get_ticket_from_database(ticket)
    
    print("\nSearching for similar tickets...")
    similar_tickets = search_for_similar_tickets(json.dumps(ticket_response))
    before = time.time()
    print("\nRunning the model...")
    
    new_ticket = build_ticket_text(ticket_response)
    similar_tickets_text = build_ticket_text_from_list(similar_tickets)

    result = CHAIN_SIMILARITY.run(new_ticket=new_ticket, similar_tickets=similar_tickets_text)
    
    context_for_question_answering["result"] = result
    context_for_question_answering["new_ticket"] = new_ticket
    context_for_question_answering["similar_tickets_text"] = similar_tickets_text

    first_time_running = True
    
    print("\nTotal time spent by the model: ", time.time() - before)

    average_story_points = get_story_points_average_from_tickets(similar_tickets)
    recommended_story_points = str(get_closest_fibonacci_number(average_story_points))
    return {"result": result + " Recommended story points: " + recommended_story_points,
            "recommended_story_points": recommended_story_points,
            "similar_tickets": [{ "ticket":item["ticket"], "summary":item["summary"], "description":item["description"], "story_points":item["story_points"], "type":item["type"] } for item in similar_tickets]}

def get_response_from_question(input) -> dict:
    global first_time_running
    if first_time_running:
        init_ai_chat_conversation(context_for_question_answering["new_ticket"],
                                  context_for_question_answering["similar_tickets_text"],
                                  context_for_question_answering["result"])
        first_time_running = False
    result = question_answering_chain.run(input)
    return {"result": result}

if __name__ == "__main__":
    ticket = '{"METHODS-105": {"summary": "Implement automated testing suite", "description": "Develop automated testing suite to automate testing of critical features and ensure software reliability and stability.", "components": ["testing automated", "devops"], "labels": ["testing", "devops", "feature"], "type": "Story", "priority": "High", "story_points": 13}}'
    tickets = search_for_similar_tickets(ticket)
    before = time.time()
    similar_tickets = ""
    number = 1
    for ticket_ in tickets:
        similar_tickets = str(ticket_) + '\n'
    result = CHAIN_SIMILARITY.run(new_ticket=ticket, similar_tickets=similar_tickets)
    #print("\nTotal time spent by the model: ", time.time() - before)
    average = get_story_points_average_from_tickets(tickets)
    recommended_story_points = "\nRecommended story points based on the similar tickets: " + str(get_closest_fibonacci_number(average))
    print(recommended_story_points)
    

#qa_chain = RetrievalQA.from_chain_type(
#    llm,
#    retriever = db.as_retriever(),
#    chain_type="stuff",
#    chain_type_kwargs = { "prompt": QA_CHAIN_PROMPT },
#)