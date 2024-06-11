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

TICKETS_SIMILARITY = PromptTemplate(
    template="""
    You are an AI assistant helping a team estimate a new ticket. The team has identified three similar tickets that can provide context for the new ticket. Based on the details of the similar tickets, provide considerations and guidance for estimating the new ticket.
    The team works in many development projects.

    New Ticket:\n
    {new_ticket}\n

    Similar Tickets:\n
    {similar_tickets}\n\n

    Please provide:
    - A summary of key similarities and differences between the tickets.
    - Important factors to consider based on the similar tickets.
    - Potential challenges and complexities that might affect the estimation.
    - Any additional guidance to help the team make an accurate estimation.

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