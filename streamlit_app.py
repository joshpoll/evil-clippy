import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from chat_data import render_chat

import langchain

langchain.verbose = False

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

st.set_page_config(page_title="HugChat - An LLM-powered Streamlit app")

# Sidebar contents
with st.sidebar:
    st.title("🤗💬 HugChat App")
    st.markdown(
        """
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [HugChat](https://github.com/Soulter/hugging-chat-api)
    - [OpenAssistant/oasst-sft-6-llama-30b-xor](https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor) LLM model
    
    💡 Note: No API key required!
    """
    )
    add_vertical_space(5)
    st.write("Made with ❤️ by [Data Professor](https://youtube.com/dataprofessor)")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        SystemMessage(
            content="Answer my questions as an unhinged philosopher who's questioning their own existence. Limit your responses to one paragraph."
        ),
        AIMessage(content="Hello, what can I help you with today?"),
    ]


# Layout of input/response containers
input_container = st.container()
colored_header(label="", description="", color_name="blue-30")
response_container = st.container()


# User input
## Function for taking user provided prompt as input
def get_text() -> str:
    input_text = st.text_input("You: ", "", key="input")
    return input_text


## Applying the user input box
with input_container:
    user_input = get_text()


# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt: str) -> str:
    st.session_state["chat_history"].append(HumanMessage(content=prompt))

    response = chat(st.session_state["chat_history"])
    st.session_state["chat_history"].append(response)
    return response


## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)

    if st.session_state["chat_history"]:
        render_chat(st.session_state["chat_history"])
