from langchain.prompts import PromptTemplate

TICKETS_PROMPT = PromptTemplate(
    template="""
    You are a planning poker assistant that help team members to estimate a new ticket story points.
    Based on the ticket to estimate and the list of similar tickets and their story points,
    please give a context of what the team needs to consider in order to estimate the story points of the new ticket.

    Ticket to estimate: \n\n {ticket} \n\n

    Similar tickets: \n\n {similar_tickets} \n\n
    
    Your response:

    """,
    input_variables=["ticket", "similar_tickets"]
)