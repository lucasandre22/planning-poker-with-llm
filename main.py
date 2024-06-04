from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from vectorstore import load_db_from_json_lines
from langchain.chains import RetrievalQA
from langchain.chains import LLMChain
from prompts import TICKETS_PROMPT, QUESTION_ANSWERING_PROMPT
from langchain_community.callbacks import get_openai_callback
import time
import json

MODEL="mistrallite:latest"

llm = Ollama(
    model=MODEL,
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
    #base_url="http://172.18.48.1:11434"
)

chain = LLMChain(llm=llm, prompt=TICKETS_PROMPT)

question_answering = LLMChain(llm=llm, prompt=QUESTION_ANSWERING_PROMPT)

def context_definer(data_retrieved_from_similarity_search):
    print("Giving context to llm...")
    
def search_for_similar_tickets(text_to_search):
    db = load_db_from_json_lines("/mnt/d/Git/trabalho-metologias-ageis/documents/tickets.jsonl", "tickets_database")
    data = db.similarity_search(text_to_search)
    tickets = []
    for page in data:
        tickets.append(json.loads(page.page_content))
    return tickets

def get_similar_tickets_story_points_average(tickets):
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

def get_response_based_on_ticket(ticket) -> dict:
    """_summary_
    Args:
        ticket (str): the ticket to search for similarity
    Returns:
        dict: JSON object containing result and recommended_story_points
    """
    tickets = search_for_similar_tickets(ticket)
    before = time.time()
    print("\nRunning the model...")
    result = chain.run(ticket=ticket, similar_tickets=tickets)
    print("\nTotal time spent by the model: ", time.time() - before)
    average = get_similar_tickets_story_points_average(tickets)
    recommended_story_points = str(get_closest_fibonacci_number(average))
    return {"result": result, "recommended_story_points": recommended_story_points}

def get_response_from_question(question) -> dict:
    result = question_answering.run(question=question)
    return {"result": result}

if __name__ == "__main__":
    ticket = '{"METHODS-105": {"summary": "Implement automated testing suite", "description": "Develop automated testing suite to automate testing of critical features and ensure software reliability and stability.", "components": ["testing automated", "devops"], "labels": ["testing", "devops", "feature"], "type": "Story", "priority": "High", "story_points": 13}}'
    tickets = search_for_similar_tickets(ticket)
    chain = LLMChain(llm=llm, prompt=TICKETS_PROMPT)

    before = time.time()
    #print("\nRunning the model...")
    similar_tickets = ""
    number = 1
    for ticket_ in tickets:
        similar_tickets = "Ticket " + str(number) + ":" + str(ticket_) + '\n'
    result = chain.run(ticket=ticket, similar_tickets=similar_tickets)
    #print("\nTotal time spent by the model: ", time.time() - before)
    average = get_similar_tickets_story_points_average(tickets)
    recommended_story_points = "\nRecommended story points based on the similar tickets: " + str(get_closest_fibonacci_number(average))
    print(recommended_story_points)
    

#qa_chain = RetrievalQA.from_chain_type(
#    llm,
#    retriever = db.as_retriever(),
#    chain_type="stuff",
#    chain_type_kwargs = { "prompt": QA_CHAIN_PROMPT },
#)