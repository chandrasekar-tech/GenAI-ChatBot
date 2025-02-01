# Chatbot with Streamlit and LangChain

This project implements a chatbot using Streamlit for the frontend and LangChain for the backend. The chatbot uses BedrockChat for language model interactions.

## Project Structure

- **`chatbot_backend.py`**: Contains the backend logic for the chatbot, including functions for model invocation, memory management, and conversation handling.
- **`chatbot_frontend.py`**: Implements the frontend using Streamlit, handling user input and displaying chat history.
- **`requirements.txt`**: Lists the Python dependencies required for the project.
- **`.vscode/settings.json`**: Contains VS Code settings for the project.

## Setup

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Running the Chatbot

1. **Start the Streamlit application:**
    ```sh
    streamlit run chatbot_frontend.py or python -m streamlit run chatbot_frontend.py
    ```

2. **Interact with the chatbot** through the web interface that opens.

## License

This project is licensed under the MIT License.