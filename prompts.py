from langchain.prompts import PromptTemplate

TICKETS_PROMPT = PromptTemplate(
    template="""
    You are a planning poker assistant that help team members to estimate a new ticket story points.
    Do not say hi or anything like this. Only give what I ask you for.
    Based on the ticket to estimate (in JSON format) and the list of similar tickets (in JSON format) and their story points,
    Give a context about the similar tickets and the ticket to estimate, also what the team needs to consider in order to estimate the story points of the new ticket.
    Based on the similar tickets, give what you found to be similar in the ticket to estimate.

    Ticket to estimate: \n\n {ticket} \n\n

    List of similar tickets: \n\n {similar_tickets} \n\n
    
    Your response:

    """,
    input_variables=["ticket", "similar_tickets"]
)

QUESTION_ANSWERING_PROMPT = PromptTemplate(
    template="""
    Answer what the user have asked
    
    Question: \n\n {question} \n\n
    
    Your response:

    """,
    input_variables=["question"]
)