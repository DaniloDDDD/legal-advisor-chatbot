from langchain_core.runnables import RunnableConfig
from langchain_openai import ChatOpenAI
from openai import api_key
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    ChatPromptTemplate)
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model = "gpt-3.5-turbo",
    api_key = OPENAI_API_KEY,
    temperature = 0
)
system_prompt = "You are an AI-powered legal advisor. Provide accurate, well-structured, and concise legal advice.Consider past conversation context when responding."

prompt_template = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_prompt),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{query}"),
])
pipeline = prompt_template | llm


chat_map = {}
def get_chat_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in chat_map:
        # if session ID doesn't exist, create a new chat history
        chat_map[session_id] = InMemoryChatMessageHistory()
    return chat_map[session_id]

pipeline_with_history = RunnableWithMessageHistory(
    pipeline,
    get_session_history=get_chat_history,
    input_messages_key="query",
    history_messages_key="history"
)

def get_legal_advice(query: str, session_id: str) -> str:
    config = RunnableConfig(configurable={"session_id": f"{session_id}"})
    return pipeline_with_history.invoke(
        {"query": f"{query}"},
        config = config
    ).content