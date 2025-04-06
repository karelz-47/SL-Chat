# SLchat: A Streamlit-Based Chatbot Using OpenAI API

SLchat is an interactive chatbot app built with Streamlit that utilizes the OpenAI API to generate responses. This app allows users to communicate with an AI model either by typing text directly or by uploading documents. In Version 8, SLchat introduces updated LLM variants and support for additional file types based on MarkItDown capabilities.

## Features

- **Text-based Chat:** Communicate with the OpenAI chatbot using text prompts.
- **File Uploads:** Upload files in various formats including PDF, DOCX, PPTX, XLSX, CSV, EPUB, images, audio, and more. The chatbot processes and analyzes the data based on your instructions.
- **Multiple AI Models:** Choose from updated LLM variants:
  - **o3-mini-2025-01-31:** Fast, flexible, intelligent reasoning model.
  - **gpt-4o-2024-08-06:** Fast, intelligent, flexible GPT model.
  - **o1-2024-12-17:** High-intelligence reasoning model.
  - **gpt-4.5-preview-2025-02-27:** Largest and most capable GPT model.
  - **o1-pro-2025-03-19:** A version of o1 with more compute for better responses.
- **Simplified Settings:** The temperature parameter has been removed to streamline the interaction experience.

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
   streamlit run SLchat_v8.py
   ```

## Usage

1. **API Key Setup:**  
   Enter your OpenAI API Key in the input box on the left sidebar. This key is required for the app to connect to the OpenAI API.

2. **Choose a Model:**  
   Select from the updated list of available AI models (e.g., `o3-mini`, `gpt-4o`, `o1`, `gpt-4.5-preview`, `o1-pro`) from the sidebar.

3. **Text Input:**  
   Enter your text prompts in the input field and press "Send" to interact with the chatbot.

4. **Upload Files:**  
   Upload documents in one of the supported formats (PDF, DOCX, PPTX, XLSX, CSV, EPUB, images, audio, etc.). Ensure your prompt instructs the AI on how to handle the file content.

## File Handling

The app now supports the following file types (and more, based on MarkItDown capabilities):

- **PDF files** (`.pdf`)
- **Word documents** (`.docx`, `.doc`)
- **Excel files** (`.xlsx`, `.xls`)
- **CSV files** (`.csv`)
- **PowerPoint presentations** (`.pptx`)
- **EPUB files** (`.epub`)
- **Images and Audio files**

Uploaded files are processed using the appropriate libraries, with MarkItDown converting their contents for the OpenAI API to analyze. You can ask the chatbot to summarize, analyze, or extract insights from the uploaded content.

## Troubleshooting

- **Missing Dependencies:**  
  Ensure all required libraries are installed by running `pip install -r requirements.txt`.
- **API Errors:**  
  Verify that your OpenAI API Key is valid and has sufficient permissions.
- **Slow Response:**  
  Depending on the selected model and file size, responses may take some time. Consider reducing file size or simplifying your prompt if necessary.

## Deploying on Streamlit Community Cloud

To deploy SLchat on Streamlit Community Cloud, ensure your repository includes:
- `SLchat_v8.py` (main script)
- `requirements.txt` (package dependencies)
- This `README.md` file

Manage your deployment from the [Streamlit Cloud Dashboard](https://share.streamlit.io).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for providing an excellent framework for building data apps.
- [OpenAI](https://openai.com/) for the powerful AI models used in this chatbot app.

---

### Additional Information

- **Version 8 Updates:**  
  - Updated LLM variants with new release dates and improved capabilities.
  - Expanded filetype support to include additional document formats, images, and audio.
  - Removed the temperature parameter for a more streamlined experience.

If you encounter any issues or have suggestions for improvement, feel free to create an issue or contribute to the project by submitting a pull request.
```

---

This README now reflects the latest version with updated model options, additional filetype support, and a simplified settings panel without the temperature parameter.
