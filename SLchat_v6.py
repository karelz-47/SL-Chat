import streamlit as st
import openai
import pandas as pd
import tiktoken

# Set page config
st.set_page_config(page_title="Custom OpenAI Chatbot", layout="wide")

# Function to define chat styles
def chat_styles():
    # Update the bubble color to match the sidebar background more closely
    SIDEBAR_BG_COLOR = '#31333F'  # Adjusted to match the sidebar background color
    st.markdown(f"""
    <style>
    .user-bubble {{
        background-color: {SIDEBAR_BG_COLOR};
        padding: 10px;
        border-radius: 15px;
        margin-bottom: 10px;
        text-align: left;
        width: fit-content;
        max-width: 80%;
        color: white;
        font-family: Arial, sans-serif;
        font-size: 14px;
        word-wrap: break-word;
    }}
    </style>
    """, unsafe_allow_html=True)

chat_styles()

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Sidebar for API key input and settings
st.sidebar.title("Settings")

# OpenAI API Key Input
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
if api_key:
    openai.api_key = api_key
else:
    st.warning("Please enter your OpenAI API Key to use the application.")

# Model selection with descriptions
model_options = {
    "GPT-4o - High-intelligence model for complex tasks": "gpt-4o",
    "GPT-4o mini - Affordable model for lightweight tasks": "gpt-4o-mini",
    "o1-preview - Beta reasoning model": "o1-preview",
    "o1-mini - Fast reasoning model": "o1-mini",
    "GPT-4 Turbo - Previous high-intelligence model": "gpt-4-turbo",
    "GPT-4 - Previous high-intelligence model": "gpt-4"
}
model_name = st.sidebar.selectbox("Choose a model", list(model_options.keys()))
selected_model = model_options[model_name]

# Define context windows and max output tokens
model_specs = {
    "gpt-4o": {"context_window": 128000, "max_output_tokens": 4096},
    "gpt-4o-mini": {"context_window": 128000, "max_output_tokens": 16384},
    "o1-preview": {"context_window": 128000, "max_output_tokens": 32768},
    "o1-mini": {"context_window": 128000, "max_output_tokens": 65536},
    "gpt-4-turbo": {"context_window": 128000, "max_output_tokens": 4096},
    "gpt-4": {"context_window": 8192, "max_output_tokens": 8192}
}

# Get selected model specs
context_window_limit = model_specs[selected_model]["context_window"]
max_output_tokens_limit = model_specs[selected_model]["max_output_tokens"]

# Model parameters
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)

# Main chat interface
st.title("🗨️ Custom OpenAI Chatbot")

# Input form
with st.form(key='input_form', clear_on_submit=True):
    user_input = st.text_area("Your message:", height=100)
    uploaded_files = st.file_uploader("Upload files (Excel or CSV)", accept_multiple_files=True, type=['xls', 'xlsx', 'csv'])
    submit_button = st.form_submit_button(label='Send')

# Handle user input
if submit_button and api_key and user_input:
    # Append user message to session state
    st.session_state['messages'].append({"role": "user", "content": user_input})

    # Prepare the conversation
    messages = st.session_state['messages']

    # Count tokens
    def count_tokens(messages, model):
        encoding = tiktoken.encoding_for_model(model)
        num_tokens = 0
        for message in messages:
            num_tokens += 4  # Every message follows <im_start>{role/name}\n{content}<im_end>\n
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
        num_tokens += 2  # Every reply is primed with <im_start>assistant
        return num_tokens

    total_tokens = count_tokens(messages, selected_model)

    # Check if total tokens exceed context window
    if total_tokens + max_output_tokens_limit > context_window_limit:
        st.error("The total tokens (input + max output) exceed the model's context window.")
        st.stop()

    try:
        # Send request to OpenAI API
        response = openai.ChatCompletion.create(
            model=selected_model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_output_tokens_limit
        )

        # Get assistant's reply
        assistant_message = response.choices[0].message['content']
        st.session_state['messages'].append({"role": "assistant", "content": assistant_message})

        # Display assistant's reply
        st.subheader("Assistant's Response")
        st.markdown(assistant_message)

    except openai.error.OpenAIError as e:
        st.error(f"OpenAI API Error: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Display conversation history
st.markdown("---")
st.subheader("Conversation History")
for idx, msg in enumerate(st.session_state['messages']):
    if msg['role'] == 'user':
        st.markdown(f"""
        <div class='user-bubble'>
            {msg['content']}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"**Assistant:** {msg['content']}")

# Security note
st.sidebar.markdown("---")
st.sidebar.markdown("⚠️ **Security Note:** Your data is processed securely in-memory and not stored.")
