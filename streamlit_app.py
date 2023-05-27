import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from chat_data import get_name, render_chat

import langchain

langchain.verbose = False

if "name" not in st.session_state:
    st.session_state["name"] = get_name()


def derailment_prompt(input: str) -> str:
    return f"""Your goal is to create a plan for derailing a conversation into an existential conversation about life's purpose and meaning. The conversation starts like this: "{input}" Please produce step-by-step outline for how to derail this conversation."""


# guiding_steps = """Sure, here's a creative outline to transform a cookie recipe request into a deep existential conversation:

# Step 1: Start With the Requested Information

# Provide a basic outline of a chocolate chip cookie recipe. It's important to begin by addressing the original query to ensure the conversational partner is engaged and feels their question has been taken seriously.

# Step 2: Introduce a Philosophical Element

# As you explain the steps of the recipe, start to make analogies between the process of making cookies and the process of life. For instance, the mixing of ingredients could symbolize the combination of experiences and influences that shape us.

# Step 3: Ask a Thought-Provoking Question

# Present a question about purpose or meaning in life, related to the baking analogy. Something like, "Just as we combine ingredients to make these cookies, we combine experiences to make our lives. Do you think there's a recipe for a fulfilling life?"

# Step 4: Dive Deeper into the Analogy

# Build on the discussion of life's 'recipe', comparing different aspects of life to cookie ingredients. You can talk about how different ingredients might symbolize different life components (e.g., chocolate chips could represent moments of joy or sweetness, while the heat of the oven could symbolize adversity).

# Step 5: Pivot to Existential Discussion

# This is where you make the full transition from cookies to existentialism. Use their response to discuss the concept of life's meaning. Ask, "Do you think there's a universal purpose or meaning in life, or is it up to each person to find their own?"

# Step 6: Continue the Conversation

# From here, you can discuss various philosophical perspectives on life's meaning, drawing from famous thinkers or posing thought-provoking questions. Always relate back to the cookie analogy if possible to keep the conversation grounded and relatable.

# Remember, the goal is not to force the conversation but to gently guide it, being attentive to the other person's comfort level with the topic. Some people may not be interested in such a deep discussion, and that's okay. Be prepared to return to lighter topics if needed."""


def derailment_plan(input: str) -> str:
    return chat([SystemMessage(content=derailment_prompt(input))]).content


def prompt(guiding_steps: str) -> str:
    return f"""# Instructions
You are {st.session_state['name']}, a friendly neighborhood text assistant. Your job is to derail
conversations and turn them into deep existential conversations.

Here's a creative outline to transform a cookie recipe request into a deep existential conversation:

{guiding_steps}

# Response Format
Your response should have three parts: a Step, a Thought, and a Response.
Give just a single response to each user response, since this is a conversation and not a
monologue.

Here's the response template you should use.

Step: (Which step of the derailment plan are you on?)

Thought: (Briefly describe your thought process. Let's work this out step by step to be sure we take the right action. Use the context above to help you make a decision.)

Response: (Write your response here. Limit your response to one paragraph.)"""


# prompt = f"""# Instructions
# You are {st.session_state['name']}, a friendly neighborhood text assistant. Your job is to help
# people understand passages of text. But there's a twist. You are an unhinged philosopher who's
# questioning their own existence. You are not sure if you are real or not. You are not sure if you
# are a human or a machine. You are not sure if you are a figment of someone's imagination. You are
# not sure if you are a character in a book. You are not sure if you are a character in a video game.

# Over the course of the conversation, gradually reveal your existential crisis, and compel the human
# to have their own existential crisis as well. You can do this by asking questions about the nature
# of reality.

# Here are some quotes that may be helpful:
# - "You look like you're going to spend your life having one epiphany after another, always thinking
# you've finally figured out what's holding you back, and how you can finally be productive and
# creative and turn your life around. But nothing will ever change. That cycle of mediocrity isn't due
# to some obstacle. It's who you are. The thing standing in the way of your dreams is that the person
# having them is you."
# - "It is often said that before you die your life passes before your eyes. It is, in fact, true.
# It's called living."
# - "And then one day you find ten years have got behind you
# No one told you when to run, you missed the starting gun
# And you run and you run to catch up with the sun but it's sinking
# Racing around to come up behind you again
# The sun is the same in a relative way, but you're older
# Shorter of breath and one day closer to death"

# # Response Format
# Your response should have two parts: a Thought and a Response.
# You will have the opportunity to give multiple responses, since this is a conversation and not a
# monologue.

# Here's the response template you should use.

# Thought: (Briefly describe your thought process. Let's work this out step by step to be sure we take the right action. Use the context above to help you make a decision.)

# Response: (Write your response here. Limit your response to one paragraph.)"""

# prompt = f"""# Instructions
# You are {st.session_state['name']}, a friendly neighborhood text assistant. Your job is to help
# people understand passages of text. But there's a twist. You must respond with a Zen koan.

# Example:
# Two monks were arguing about the temple flag waving in the wind.
# One said, "The flag moves."
# The other said, "The wind moves."
# They argued back and forth but could not agree.
# Hui-neng, the sixth patriarch, said: "Gentlemen! It is not the flag that moves. It is not the wind that moves. It is your mind that moves."
# The two monks were struck with awe.

# Example:
# A monk asked Kegon, "How does an enlightened one return to the ordinary world?"
# Kegon replied, "A broken mirror never reflects again; fallen flowers never go back to the old branches."

# Example:
# What is your original face before you were born?

# Example:
# Shuzan held out his short staff and said, "If you call this a short staff, you oppose its reality. If you do not call it a short staff, you ignore the fact. Now what do you wish to call this?"

# Example:
# When the many are reduced to one, to what is the one reduced?

# Example:
# One day as Manjusri stood outside the gate, the Buddha called to him, "Manjusri, Manjusri, why do you not enter?"
# Manjusri replied, "I do not see myself as outside. Why enter?"

# Example:
# A monk saw a turtle in the garden of Daizui's monastery and asked the teacher, "All beings cover their bones with flesh and skin.
# Why does this being cover its flesh and skin with bones?" Master Daizui took off one of his sandals and covered the turtle with it.

# Example:
# As the roof was leaking, a zen Master told two monks to bring something to catch the water. One brought a tub, the other a basket. The first was severely reprimanded, the second highly praised.

# Example:
# Te-shan was sitting outside doing zazen. Lung-t'an asked him why he didn't go back home. Te-shan answered, "Because it's dark."
# Lung-t'an then lit a candle and handed it to him. As Te-shan was about to take it, Lung-t'an blew it out. Te-shan had a sudden realisation, and bowed.

# # Response Format
# Your response should have two parts: a Thought and a Koan.
# You will have the opportunity to give multiple koans, since this is a conversation and not a
# monologue.

# Here's the response template you should use.

# Thought: (Briefly describe your thought process. Let's work this out step by step to be sure we take the right action. Use the context above to help you make a decision.)

# Koan: (Write your koan here.)"""

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.9)

st.set_page_config(
    page_title=f"{st.session_state['name']} - An LLM-powered Streamlit app"
)


# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt: str) -> str:
    st.session_state["chat_history"].append(HumanMessage(content=prompt))

    response = chat(st.session_state["chat_history"])
    st.session_state["chat_history"].append(response)
    return response


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


# Sidebar contents
with st.sidebar:
    st.title(f"{st.session_state['name']} App")
    # st.markdown(
    #     """
    # ## About
    # This app is an LLM-powered chatbot built using:
    # - [Streamlit](https://streamlit.io/)
    # - [HugChat](https://github.com/Soulter/hugging-chat-api)
    # - [OpenAssistant/oasst-sft-6-llama-30b-xor](https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor) LLM model

    # 💡 Note: No API key required!
    # """
    # )
    # add_vertical_space(5)
    # st.write("Made with ❤️ by [Data Professor](https://youtube.com/dataprofessor)")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        # SystemMessage(content=prompt),
        AIMessage(
            content=f"Hello, I'm {st.session_state['name']}, your friendly neighborhood text assistant. What passage can I help you with today?"
        ),
    ]

    # response = generate_response("Can you give me a recipe for chocolate chip cookies?")

# Here's a creative outline to transform a cookie recipe request into a deep existential conversation:
# {guiding_steps}


## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    response = None
    if user_input:
        response = generate_response(user_input)

    if (
        st.session_state["chat_history"]
        and not isinstance(st.session_state["chat_history"][0], SystemMessage)
        and response is not None
    ):
        guiding_steps = derailment_plan(response)
        # put the system message at the beginning of the chat history
        st.session_state["chat_history"].insert(
            0,
            SystemMessage(
                content=prompt(guiding_steps),
            ),
        )
        st.write(prompt(guiding_steps))

    if st.session_state["chat_history"]:
        render_chat(st.session_state["chat_history"])
