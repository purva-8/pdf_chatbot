import pdfplumber
import os
import uuid
from services.embedding_service import generate_and_save_embeddings
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

# extract text and save embeddings
def process_pdf_upload(uploaded_file):
    pdf_id = str(uuid.uuid4())
    file_path = f'../data/uploads/{pdf_id}.pdf'
    
    # Save the uploaded file with a unique ID
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    
    extracted_text = extract_text_from_pdf(file_path)
    
    
    embedding_file_path = generate_and_save_embeddings(pdf_id, extracted_text)

    # Return metadata
    pdf_data = {
        "name": uploaded_file.name,
        "path": file_path,
        "embeddings_path": embedding_file_path,
        "text": extracted_text
    }
    
    return pdf_id, pdf_data

# extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""

    try:
    
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

    except Exception as e:
        print(f"Error with pdfplumber: {e}")

    #If no text was extracted, use OCR as a fallback
    if not text.strip():
        print("No text extracted with pdfplumber. Falling back to OCR.")
        text = extract_text_with_ocr(pdf_path)

    return text

# Fallback OCR function for image-based PDFs
def extract_text_with_ocr(pdf_path):
    text = ""

    try:
        # Convert PDF pages to images
        images = convert_from_path(pdf_path)
        
        # Perform OCR on each page image
        for image in images:
            text += pytesseract.image_to_string(image) + "\n"

    except Exception as e:
        print(f"Error during OCR: {e}")

    return text
