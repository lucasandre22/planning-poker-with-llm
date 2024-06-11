from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from prompts import TICKETS_PROMPT, QUESTION_ANSWERING_PROMPT, TICKETS_SIMILARITY

MODEL="mistrallite:latest"

llm = Ollama(
    model=MODEL,
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
    #base_url="http://172.18.48.1:11434"
)

CHAIN = LLMChain(llm=llm, prompt=TICKETS_PROMPT)

CHAIN_SIMILARITY = LLMChain(llm=llm, prompt=TICKETS_SIMILARITY)


QUESTION_ANSWERING_CHAIN = LLMChain(llm=llm, prompt=QUESTION_ANSWERING_PROMPT)