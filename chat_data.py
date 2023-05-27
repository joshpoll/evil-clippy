from typing import List
from langchain.schema import BaseMessage, HumanMessage, SystemMessage, AIMessage
from streamlit_chat import message
import random


ChatHistory = List[BaseMessage]


def parse_response(content: str) -> str:
    # the input content has Thought: and Response: sections. We should strip out the Thought:
    # section and return the Response: section. To do this, we'll split the string at the
    # "Response:"
    # if "Response:" in content:
    #     content = content.split("Response:")[1]
    return content


def render_chat(history: ChatHistory):
    for i, msg in enumerate(history):
        if isinstance(msg, HumanMessage):
            message(msg.content, is_user=True, key=str(i) + "_user")
        elif isinstance(msg, AIMessage):
            content = parse_response(msg.content)
            message(content, key=str(i))


names = [
    "Book Beacon",
    "LiteraLens",
    "Text Navigator",
    "Comprehend Companion",
    "Page Sage",
    "Clarity Quill",
    "Parse Partner",
    "Prose Paladin",
    "Verse Vantage",
    "Scroll Squire",
    "Codex Comrade",
    "Lexicon Liaison",
    "Context Companion",
    "Passage Pathfinder",
    "ReadRiddle Resolver",
    "Insight Inkwell",
    "Annotation Ally",
    "Wisdom Weave",
    "Sentiment Sherpa",
    "Phrase Pharaoh",
    "Extract Elf",
    "Tome Tamer",
    "Insight Invoker",
    "Chapter Chaperone",
    "Discourse Decoder",
]


def get_name():
    # pick randomly from names
    return random.choice(names)
