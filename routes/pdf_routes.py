import streamlit as st
from services.pdf_service import process_pdf_upload
from services.embedding_service import generate_and_save_embeddings
from utils.metadata_utils import load_metadata, save_metadata_safely
import os

UPLOAD_FOLDER = 'uploads'  # Directory to save uploaded files


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# PDF upload and processing
def handle_pdf_upload():
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")
    pdf_metadata = load_metadata('pdf_metadata.json')

    if uploaded_file:
        
        file_extension = uploaded_file.name.split('.')[-1].lower()  

        st.write(f"Uploaded file extension: {file_extension}")

        # Check for correct file extension 
        if file_extension != "pdf":
            st.error(f"Invalid file type. You uploaded a file with the extension '.{file_extension}', which is not a PDF. Please upload a PDF file.")  
            return pdf_metadata 

        file_name = uploaded_file.name
        
        # Check if the file already exists 
        existing_pdf_id = None
        for pdf_id, data in pdf_metadata.items():
            if data["name"] == file_name:
                existing_pdf_id = pdf_id
                break
        
        if existing_pdf_id:
            # If the PDF already exists, return the existing metadata
            st.success(f"The PDF '{file_name}' is already uploaded and available!")
            return pdf_metadata 
        else:
            # Process the PDF to generate metadata
            pdf_id, pdf_data = process_pdf_upload(uploaded_file)

            # Save the PDF in the UPLOAD_FOLDER using its pdf_id
            file_path = os.path.join(UPLOAD_FOLDER, f"{pdf_id}.pdf")
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())  
            
            # Add file path to the metadata
            pdf_data["file_path"] = file_path

            # Save the new metadata
            save_metadata_safely(pdf_id, pdf_data, 'pdf_metadata.json')
            pdf_metadata[pdf_id] = pdf_data
            
            st.success(f"File '{file_name}' uploaded and processed successfully!")

    return pdf_metadata
