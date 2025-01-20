import streamlit as st
from services.chat_service import generate_chat_response

# Chat functionality
def handle_chat(pdf_data):
    # Get the user's question
    question = st.text_input("Ask a question:")
    
    # Load chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if question:
        # Generate bot response based on the user's question and PDF data
        response = generate_chat_response(question, pdf_data)
        
        # Add the exchange to chat history
        st.session_state.chat_history.append({"question": question, "answer": response})

    # Display chat history
    for exchange in st.session_state.chat_history:
        st.write(f"**You:** {exchange['question']}")
        st.write(f"**Bot:** {exchange['answer']}")
