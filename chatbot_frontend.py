# Source: Below code is provided by Streamlit and AWS

#1 import streamlit and chatbot file
import streamlit as st
import chatbot_backend as demo  # Import your Chatbot file as demo

#2 Set Title for Chatbot
st.title("Hi, Any questions?")  # Modify this based on the title you want

#3 LangChain memory to the session cache - Session State
if 'memory' not in st.session_state:
    st.session_state.memory = demo.demo_memory()  # Modify the import and memory function() attributes to initialize the memory

#4 Add the UI chat history to the session cache - Session State
if 'chat_history' not in st.session_state:  # See if the chat history hasn't been created yet
    st.session_state.chat_history = []  # Initialize the chat history

#5 Re-render the chat history (Streamlit re-runs this script, so need this to preserve previous chat messages)
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

#6 Enter the details for chatbot input box
input_text = st.chat_input("Type here...")  # Display a chat input box
if input_text:
    with st.chat_message("user"):
        st.markdown(input_text)

    st.session_state.chat_history.append({"role": "user", "text": input_text})

    chat_response = demo.demo_chatbot().predict(input_text)  # Replace with demo_chatbot().predict(input_text) - call the model through the supporting library

    with st.chat_message("assistant"):
        st.markdown(chat_response)

    st.session_state.chat_history.append({"role": "assistant", "text": chat_response})
