# GenAI-Chatbot with Streamlit and LangChain

**GenAI-Chatbot** is a chatbot application that utilizes **Streamlit** for the frontend and **LangChain** for the backend. The chatbot integrates with **AWS Bedrock** for language model interactions, enabling intelligent and dynamic conversations.

## Features
- Conversational AI chatbot powered by **LangChain**.
- Interactive web-based UI built with **Streamlit**.
- **AWS Bedrock** integration for natural language responses.
- Supports conversation memory for contextual awareness.
- Easy setup and deployment.

## Project Structure
- README.md
- requirements.txt         # Python dependencies
- .vscode/settings.json    # VS Code settings (optional)
- src/
    - chatbot_backend.py   # Backend logic for model invocation, memory management, and conversation handling.
    - chatbot_frontend.py  # Streamlit-based frontend for user interaction.

## Requirements
- Python 3.8+
- AWS credentials configured in ~/.aws/config and ~/.aws/credentials
- Refer to the Requirements.txt for other dependencies
  
## Setup
Clone the repository:
    - git clone <repository-url>
    - cd <repository-directory>
    
Install the dependencies:
    pip install -r requirements.txt

## Running the Chatbot
Start the Streamlit application:
    - streamlit run chatbot_frontend.py or python -m streamlit run chatbot_frontend.py
    - Interact with the chatbot through the web interface that opens in your browser.

## Configuration
Ensure your AWS credentials are correctly configured in ~/.aws/config and ~/.aws/credentials:
~/.aws/config:
[default]
region = us-east-1

## License
This project is licensed under the MIT License.

## Disclaimer
This project is a personal Proof of Concept (PoC) to explore Generative AI capabilities using LangChain and AWS Bedrock. It is not designed for production use and does not conform to enterprise standards.
