import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat

import streamlit as st

st.set_page_config(page_title="HugChat - An LLM-powered Streamlit app")

with st.sidebar:
    st.title("🤗💬 HugChat App")
    st.markdown(
        """
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](<https://streamlit.io/>)
    - [HugChat](<https://github.com/Soulter/hugging-chat-api>)
    - [OpenAssistant/oasst-sft-6-llama-30b-xor](<https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor>) LLM model
    
    💡 Note: No API key required!
    """
    )
    add_vertical_space(5)
    st.write("Made with ❤️ by [Data Professor](<https://youtube.com/dataprofessor>)")

if "generated" not in st.session_state:
    st.session_state["generated"] = ["I'm HugChat, How may I help you?"]

if "past" not in st.session_state:
    st.session_state["past"] = ["Hi!"]

input_container = st.container()
colored_header(label="", description="", color_name="blue-30")
response_container = st.container()
