from typing import List
from langchain.schema import BaseMessage, HumanMessage, SystemMessage, AIMessage
from streamlit_chat import message


ChatHistory = List[BaseMessage]


def render_chat(history: ChatHistory):
    for i, msg in enumerate(history):
        if isinstance(msg, HumanMessage):
            message(msg.content, is_user=True, key=str(i) + "_user")
        elif isinstance(msg, AIMessage):
            message(msg.content, key=str(i))
