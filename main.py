
from vectorstore import search_for_similar_tickets
from ticket_handling import build_ticket_text, build_ticket_text_from_list
from llm import CHAIN, QUESTION_ANSWERING_CHAIN, CHAIN_SIMILARITY
import time

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

def get_response_based_on_ticket(ticket: dict) -> dict:
    """_summary_
    Args:
        ticket (str): the ticket to search for similarity
    Returns:
        dict: JSON object containing result and recommended_story_points
    """
    similar_tickets = search_for_similar_tickets(ticket)
    before = time.time()
    print("\nRunning the model...")
    result = CHAIN_SIMILARITY.run(new_ticket=build_ticket_text(ticket),
                                  similar_tickets=build_ticket_text_from_list(similar_tickets))
    print("\nTotal time spent by the model: ", time.time() - before)
    average = get_story_points_average_from_tickets(similar_tickets)
    recommended_story_points = str(get_closest_fibonacci_number(average))
    return {"result": result,
            "recommended_story_points": recommended_story_points,
            "similar_tickets": [{ "ticket":item["ticket"], "summary":item["summary"], "description":item["description"] } for item in similar_tickets]}

def get_response_from_question(input) -> dict:
    result = QUESTION_ANSWERING_CHAIN.run(input)
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