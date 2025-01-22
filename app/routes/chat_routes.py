import streamlit as st
import os
import json
from services.chat_service import generate_chat_response

CHAT_HISTORY_FOLDER = "../data/chat_history"

if not os.path.exists(CHAT_HISTORY_FOLDER):
    os.makedirs(CHAT_HISTORY_FOLDER)

# Load the chat history from a file
def load_chat_history(pdf_id):
    file_path = os.path.join(CHAT_HISTORY_FOLDER, f"chat_history_{pdf_id}.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return []

# save the chat history to a file
def save_chat_history(pdf_id, chat_history):
    file_path = os.path.join(CHAT_HISTORY_FOLDER, f"chat_history_{pdf_id}.json")
    with open(file_path, "w") as file:
        json.dump(chat_history, file, indent=4)

#chat functionality
def handle_chat(pdf_id, pdf_data):

    if "chat_histories" not in st.session_state:
        st.session_state.chat_histories = {}


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
        args=(pdf_id, pdf_data, chat_history),
    )

# question submission
def handle_question_submit(pdf_id, pdf_data, chat_history):
    question = st.session_state[f"text_input_{pdf_id}"]

    if question.strip():
        response = generate_chat_response(question, pdf_data)


        chat_history.append({"question": question, "answer": response})


        save_chat_history(pdf_id, chat_history)

        # Add the exchange to session state chat history
        st.session_state.chat_histories[pdf_id] = chat_history

        # Clear the input field after submission
        st.session_state[f"question_{pdf_id}"] = ""
