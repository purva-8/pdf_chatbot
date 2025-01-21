import streamlit as st
import os
import json
from services.chat_service import generate_chat_response

# Define the folder to store chat history files
CHAT_HISTORY_FOLDER = "chat_history"

# Ensure the folder exists
if not os.path.exists(CHAT_HISTORY_FOLDER):
    os.makedirs(CHAT_HISTORY_FOLDER)

# Define a function to load the chat history from a file
def load_chat_history(pdf_id):
    file_path = os.path.join(CHAT_HISTORY_FOLDER, f"chat_history_{pdf_id}.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return []

# Define a function to save the chat history to a file
def save_chat_history(pdf_id, chat_history):
    file_path = os.path.join(CHAT_HISTORY_FOLDER, f"chat_history_{pdf_id}.json")
    with open(file_path, "w") as file:
        json.dump(chat_history, file, indent=4)

# Route to handle chat functionality
def handle_chat(pdf_id, pdf_data):
    # Ensure 'chat_histories' is initialized in session state
    if "chat_histories" not in st.session_state:
        st.session_state.chat_histories = {}

    # Load the chat history from the file
    chat_history = load_chat_history(pdf_id)

    # Display chat history for the selected PDF
    for exchange in chat_history:
        st.write(f"**You:** {exchange['question']}")
        st.write(f"**Bot:** {exchange['answer']}")

    # Use session state to manage the text input
    if f"question_{pdf_id}" not in st.session_state:
        st.session_state[f"question_{pdf_id}"] = ""

    # Text input for asking questions
    question = st.text_input(
        "Ask a question:",
        key=f"text_input_{pdf_id}",
        value=st.session_state[f"question_{pdf_id}"],
        on_change=handle_question_submit,
        args=(pdf_id, pdf_data, chat_history),  # Pass the current chat history
    )

# Helper function to handle the question submission
def handle_question_submit(pdf_id, pdf_data, chat_history):
    question = st.session_state[f"text_input_{pdf_id}"]  # Get the current input

    if question.strip():  # Ensure the question is not empty
        # Generate bot response based on the user's question and PDF data
        response = generate_chat_response(question, pdf_data)

        # Add the exchange to the chat history for the selected PDF
        chat_history.append({"question": question, "answer": response})

        # Save the updated chat history to the file
        save_chat_history(pdf_id, chat_history)

        # Add the exchange to session state chat history
        st.session_state.chat_histories[pdf_id] = chat_history

        # Clear the input field after submission
        st.session_state[f"question_{pdf_id}"] = ""
