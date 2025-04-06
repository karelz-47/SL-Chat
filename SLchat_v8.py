import streamlit as st
from openai import OpenAI, APIConnectionError, APIError
from markitdown import MarkItDown
import tempfile

# Initialize MarkItDown
mid = MarkItDown()

# Set page config
st.set_page_config(page_title="Custom OpenAI Chatbot", layout="wide")

# Function to define chat styles
def chat_styles():
    SIDEBAR_BG_COLOR = '#31333F'
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
    client = OpenAI(api_key=api_key)
else:
    st.sidebar.warning("Enter your API Key to send messages.")

###############################################################################
# UPDATED MODEL LIST, DESCRIPTIONS, AND LIMITS
###############################################################################

# Model usage limits (for reference, if you need them)
model_limits = {
    "gpt-4o-2024-08-06": {
        "TPM": 2_000_000,  # tokens per minute
        "RPM": 10_000      # requests per minute
    },
    "o3-mini-2025-01-31": {
        "TPM": 10_000_000,
        "RPM": 10_000
    },
    "o1-pro-2025-03-19": {
        "TPM": 2_000_000,
        "RPM": 10_000
    },
    "o1-2024-12-17": {
        "TPM": 2_000_000,
        "RPM": 10_000
    },
    "gpt-4.5-preview-2025-02-27": {
        "TPM": 1_000_000,
        "RPM": 10_000
    }
}

# Model selection with descriptions
model_options = {
    "o3-mini (Fast, flexible, intelligent reasoning model)": "o3-mini-2025-01-31",
    "gpt-4o (Fast, intelligent, flexible GPT model)": "gpt-4o-2024-08-06",
    "o1 (High-intelligence reasoning model)": "o1-2024-12-17",
    "gpt-4.5-preview (Largest and most capable GPT model)": "gpt-4.5-preview-2025-02-27",
    "o1-pro (More compute for better responses)": "o1-pro-2025-03-19"
}

# For each model, define your context window and max output tokens as needed.
model_specs = {
    "o3-mini-2025-01-31": {"context_window": 128000, "max_output_tokens": 16384},
    "gpt-4o-2024-08-06": {"context_window": 128000, "max_output_tokens": 4096},
    "o1-2024-12-17": {"context_window": 128000, "max_output_tokens": 16384},
    "gpt-4.5-preview-2025-02-27": {"context_window": 128000, "max_output_tokens": 16384},
    "o1-pro-2025-03-19": {"context_window": 128000, "max_output_tokens": 16384}
}
###############################################################################

model_name = st.sidebar.selectbox("Choose a model", list(model_options.keys()))
selected_model = model_options[model_name]

# Grab the relevant specs for the chosen model
context_window_limit = model_specs[selected_model]["context_window"]
max_output_tokens_limit = model_specs[selected_model]["max_output_tokens"]

# Main chat interface
st.title("🗨️ Custom OpenAI Chatbot")

with st.form(key='input_form', clear_on_submit=True):
    user_input = st.text_area("Your message:", height=100)
    uploaded_files = st.file_uploader(
        "Upload files (PDF, DOCX, PPTX, XLSX, CSV, EPUB, images, audio, etc.)",
        accept_multiple_files=True
    )
    submit_button = st.form_submit_button(label='Send')

if submit_button and user_input:
    st.session_state['messages'].append({"role": "user", "content": user_input})

    if uploaded_files:
        file_content_list = []
        for uploaded_file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_file_path = tmp_file.name
            try:
                result = mid.convert(tmp_file_path)
                markdown_content = result.text_content
                file_content_list.append(markdown_content)
            except Exception as e:
                st.warning(f"Could not process file {uploaded_file.name}: {e}")
        if file_content_list:
            combined_file_content = "\n\n".join(file_content_list)
            st.session_state['messages'].append(
                {"role": "user", "content": f"File data:\n{combined_file_content}"}
            )

    if not api_key:
        st.error("Please enter your API key.")
    else:
        # Decide which parameter to send to the API
        # Typically "max_tokens" is for GPT-4-like models,
        # "max_completion_tokens" for the 'o' series. Adjust as needed.
        if selected_model.startswith(("o1", "o3")):
            token_param = {"max_completion_tokens": max_output_tokens_limit}
        else:
            token_param = {"max_tokens": max_output_tokens_limit}

        api_params = {
            "model": selected_model,
            "messages": st.session_state['messages']
        }
        api_params.update(token_param)

        try:
            response = client.chat.completions.create(**api_params)
            assistant_message = response.choices[0].message.content
            st.session_state['messages'].append({"role": "assistant", "content": assistant_message})
            st.subheader("Assistant's Response")
            st.markdown(assistant_message)
        except (APIConnectionError, APIError) as e:
            st.error(f"OpenAI API Error: {e}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

st.markdown("---")
st.subheader("Conversation History")
for msg in st.session_state['messages']:
    if msg['role'] == 'user':
        st.markdown(f"<div class='user-bubble'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"**Assistant:** {msg['content']}")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🆕 Version 8 Updates")
st.sidebar.markdown("- Updated LLM variants available: o3 mini, GPT-4o, o1, GPT-4.5, o1 Pro")
st.sidebar.markdown("- New filetypes processed: PDF, DOCX, PPTX, XLSX, CSV, EPUB, images, audio, etc.")
st.sidebar.markdown("---")
st.sidebar.markdown("⚠️ **Security Note:** Data is securely processed in-memory and not stored.")
