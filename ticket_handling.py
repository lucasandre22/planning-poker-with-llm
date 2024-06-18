
def build_ticket_text_from_list(tickets: list[str]) -> str:
    tickets_text = ""
    for ticket in tickets:
        tickets_text += build_ticket_text(ticket)
    return tickets_text

def build_ticket_text(ticket: str) -> str:
    """
    """
    return f"""
    Ticket ID: {ticket['ticket']}
    Summary: {ticket['summary']}
    Description: {ticket['description']}
    Components: {ticket['components']}
    Labels: {ticket['labels']}
    Type: {ticket['type']}
    Priority: {ticket['priority']}
    Story Points: {ticket['story_points']}
    \n"""