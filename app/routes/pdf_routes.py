import streamlit as st
from services.pdf_service import process_pdf_upload
from services.embedding_service import generate_and_save_embeddings
from utils.metadata_utils import load_metadata, save_metadata_safely
import os

UPLOAD_FOLDER = "../data/uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# PDF upload and processing
def handle_pdf_upload():
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")
    pdf_metadata = load_metadata('../data/pdf_metadata.json')

    if uploaded_file:
        
        file_name = uploaded_file.name
        
        
        existing_pdf_id = None
        for pdf_id, data in pdf_metadata.items():
            if data["name"] == file_name:
                existing_pdf_id = pdf_id
                break
        
        if existing_pdf_id:
            
            st.success(f"The PDF '{file_name}' is already uploaded and available!")
            return pdf_metadata 
        else:
            #generate its ID and metadata
            pdf_id, pdf_data = process_pdf_upload(uploaded_file)

            # Save the uploaded file using its unique pdf_id
            file_path = os.path.join(UPLOAD_FOLDER, f"{pdf_id}.pdf")
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())  # Save the file content
            
            # Add file path to the metadata
            pdf_data["file_path"] = file_path

            # Save the new metadata
            save_metadata_safely(pdf_id, pdf_data, '../data/pdf_metadata.json')
            pdf_metadata[pdf_id] = pdf_data
            
            st.success(f"File '{file_name}' uploaded and processed successfully!")

    return pdf_metadata
