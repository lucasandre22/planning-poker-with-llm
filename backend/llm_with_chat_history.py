from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from prompts import QA_SYSTEM_PROMPT

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]

class LLMWithChatHistory:
    def __init__(self, llm, new_ticket, similar_tickets, ai_response):
        self.store = {}

        qa_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    QA_SYSTEM_PROMPT.format(new_ticket=new_ticket, similar_tickets=similar_tickets, ai_response=ai_response)
                ),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{input}"),
            ]
        )
        self.runnable = qa_prompt | llm
        self.chain_with_message_history = RunnableWithMessageHistory(
            self.runnable,
            get_session_history,
            input_messages_key="input",
            history_messages_key="history",
        )
        
    def run(self, input, session_id="abc123"):
        result = self.chain_with_message_history.invoke(
            {"input": input},
            config={"configurable": {"session_id": session_id}},
        )
        return result

"""References:
https://python.langchain.com/v0.1/docs/expression_language/how_to/message_history/
https://python.langchain.com/v0.2/docs/how_to/qa_chat_history_how_to/
"""