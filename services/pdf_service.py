import pdfplumber
import os
import uuid
from services.embedding_service import generate_and_save_embeddings

# Process the PDF file 
def process_pdf_upload(uploaded_file):
    pdf_id = str(uuid.uuid4())
    file_path = f'uploads/{pdf_id}.pdf'
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    extracted_text = extract_text_from_pdf(file_path)
    embedding_file_path = generate_and_save_embeddings(pdf_id, extracted_text)

    pdf_data = {
        "name": uploaded_file.name,
        "path": file_path,
        "embeddings_path": embedding_file_path,
        "text": extracted_text
    }
    
    return pdf_id, pdf_data

# Text Extraction 
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text
