import streamlit as st
from routes.chat_routes import handle_chat  # Import the handle_chat function from chat service
from routes.pdf_routes import handle_pdf_upload  # Assuming you have a pdf_service.py to handle PDF uploads and metadata loading

# Sidebar for PDF upload and selection (left side)
with st.sidebar:
    st.title("AI-Powered PDF Chatbot")
    st.header("Upload & Select PDF")

    # Handle PDF upload and metadata load
    pdf_metadata = handle_pdf_upload()

    if not pdf_metadata:
        st.info("No PDFs uploaded yet.  \nPlease upload a PDF to get started.")

    # Radio button list to select a PDF only if metadata exists
    selected_pdf_name = None  # Initialize the variable here
    if pdf_metadata:
        selected_pdf_name = st.radio(
            "Select a PDF to chat with:",
            [pdf_metadata[key]["name"] for key in pdf_metadata],
            horizontal=True  # Display options horizontally
        )

# Main content area (right side) for the chat interface
if selected_pdf_name:
    # Find the pdf_id corresponding to the selected name
    selected_pdf_id = next(key for key, value in pdf_metadata.items() if value["name"] == selected_pdf_name)

    # Retrieve the data for the selected PDF
    selected_pdf_data = pdf_metadata[selected_pdf_id]

    # Display the message at the top of the chat section
    st.write(f"### You are now chatting with **{selected_pdf_name}**")

    # Call the function to handle the chat for the selected PDF
    handle_chat(selected_pdf_id, selected_pdf_data)  # Pass `selected_pdf_id` and `selected_pdf_data`

else:
    st.info("Please select a PDF to start chatting.")
