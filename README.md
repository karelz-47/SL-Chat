# SLchat: A Streamlit-Based Chatbot Using OpenAI API

SLchat is an interactive chatbot app built with Streamlit that utilizes the OpenAI API to generate responses. This app allows users to communicate with an AI model and upload text or Excel files for processing. The chatbot can handle various tasks based on user prompts and respond accordingly.

## Features

- **Text-based Chat:** Communicate with the OpenAI chatbot using text prompts.
- **File Uploads:** Upload text (CSV) or Excel files, and the chatbot will process and analyze the data based on your instructions.
- **Multiple AI Models:** Choose from different OpenAI models, including `GPT-4o`, `GPT-4o-mini`, `GPT-4 Turbo`, and more.
- **Customizable Parameters:** Adjust settings like temperature to influence the chatbot's creativity.

## Installation

Follow these steps to run the app locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/karelz-47/SLchat.git
   cd SLchat
   ```

2. **Install the required packages:**
   Make sure you have Python 3.7+ installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run SLchat_v7.py
   ```

## Usage

1. **API Key Setup:** Enter your OpenAI API Key in the input box on the left sidebar. This is required for the app to connect to the OpenAI API.
2. **Choose a Model:** Select from the available OpenAI models (e.g., `GPT-4o`, `GPT-4o-mini`) from the sidebar.
3. **Set Parameters:** Adjust the temperature slider to control the creativity of the AI's responses.
4. **Text Input:** Enter your text prompts in the input field and press "Submit" to interact with the chatbot.
5. **Upload Files:** Upload CSV or Excel files for the AI to process. Make sure your prompt instructs the AI on how to handle the file data.

## File Handling

The app supports the following file types:
- **CSV files** (`.csv`)
- **Excel files** (`.xlsx`)

Uploaded files are read using `pandas` and processed by the OpenAI API based on your prompts. For example, you can ask the chatbot to summarize data from an uploaded file.

## Troubleshooting

- **Missing Dependencies:** Ensure all required libraries are installed by running `pip install -r requirements.txt`.
- **API Errors:** Make sure your OpenAI API Key is valid and has sufficient permissions.
- **Slow Response:** Depending on the model and data size, responses may take some time. You can try reducing the file size or using a simpler prompt.

## Deploying on Streamlit Community Cloud

If you'd like to deploy the app on Streamlit Community Cloud, make sure your repository is connected and contains all necessary files:
- `SLchat_v7.py` (main script)
- `requirements.txt` (package dependencies)
- This `README.md` file

You can manage your deployment from the [Streamlit Cloud Dashboard](https://share.streamlit.io).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for providing a great framework for building data apps.
- [OpenAI](https://openai.com/) for the powerful AI models used in this chatbot app.

---

### Additional Information

If you encounter any issues or have suggestions for improvement, feel free to create an issue or contribute to the project by submitting a pull request.
