import streamlit as st
from routes.chat_routes import handle_chat  
from routes.pdf_routes import handle_pdf_upload  

# Sidebar for PDF upload and selection 
with st.sidebar:
    st.title("AI-Powered PDF Chatbot")
    st.header("Upload & Select PDF")

    # PDF upload and metadata load
    pdf_metadata = handle_pdf_upload()

    if not pdf_metadata:
        st.info("No PDFs uploaded yet. Please upload a PDF to get started.")


    selected_pdf_name = None  
    if pdf_metadata:
        selected_pdf_name = st.radio(
            "Select a PDF to chat with:",
            [pdf_metadata[key]["name"] for key in pdf_metadata] if pdf_metadata else [],
            horizontal=True  # Display the options horizontally 
        )

# Chat interface
if selected_pdf_name:

    selected_pdf_id = next(key for key, value in pdf_metadata.items() if value["name"] == selected_pdf_name)

    # Message at the top of the chat section
    st.write(f"### You are now chatting with **{selected_pdf_name}**")


    handle_chat(pdf_metadata[selected_pdf_id])

else:
    st.info("Please select a PDF to start chatting.")
