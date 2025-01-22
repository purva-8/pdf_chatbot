# Chatbot Application Documentation

## Overview
This chatbot application is designed to provide interactive and intelligent responses to user queries. It leverages NLP models for generating embeddings, retrieving relevant information, and facilitating seamless conversations. The application is built using Python and integrates several services and utilities for efficiency.

### Features
- **Interactive Chat**: Responds to user queries with contextual and relevant answers.
- **PDF Upload and Processing**: Users can upload PDF documents which are processed further.
- **Embedding Service**: Converts text into embeddings for similarity calculations and retrieval tasks.
- **API Integration**: Exposes endpoints for chat and PDF-related operations.
- **Customizable Configurations**: Includes a configuration file for easy customization of settings.

---

## Setup Instructions

### Prerequisites
1. **Python**: Ensure Python 3.8 or higher is installed.
2. **Virtual Environment**: It is recommended to use a virtual environment for dependency management.
3. **Dependencies**: Install the required libraries listed in `requirements.txt`.

### Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the application:
   - Update `utils/config.py` for application-specific configurations.

5. Run the application:
   ```bash
   streamlit run app.py
   ```

6. Access the application:
   Open your browser and navigate to `http://localhost:8501`.

---
## Docker Setup Instructions
To run the application using Docker, make sure Docker is installed on your system. Follow the steps below:

1. Build the Docker image:
   ```bash
   docker build -t streamlit-app .
   ```
2. Create and run the Docker container:
   ```bash
   docker run -itd --name pdf-chatbot -p 8051:801 streamlit-app
   ```
3. View the Running Container:
   ```bash
   docker ps
   ```
4. View logs for troubleshooting:
   ```bash
   docker logs <container-id-of-pdf-chatbot>
   ```
5. Access the application:
    Paste the network URL provided in the logs into your browser, and the application will be running!

## API Documentation

### Base URL
`http://localhost:8501`

### Endpoints

#### 1. **Chat Endpoint**
   - **URL**: `/chat`
   - **Method**: POST
   - **Description**: Handles user queries and returns chatbot responses.
   - **Request Body**:
     ```json
     {
       "query": "<user_query>"
     }
     ```
   - **Response**:
     ```json
     {
       "response": "<chatbot_response>"
     }
     ```

#### 2. **PDF Upload Endpoint**
   - **URL**: `/upload-pdf`
   - **Method**: POST
   - **Description**: Allows users to upload PDF files for information retrieval.
   - **Request Body**:
     - Form-data with key `file` containing the PDF.
   - **Response**:
     ```json
     {
       "status": "success",
       "message": "PDF uploaded successfully."
     }
     ```

#### 3. **Retrieve PDF Metadata**
   - **URL**: `/pdf-metadata`
   - **Method**: GET
   - **Description**: Fetches metadata of uploaded PDFs.
   - **Response**:
     ```json
     {
       "pdf_id": [
         {
           "name": "pdf_name",
           "path": "pdf_path",
           "embeddings_path": "embeddings_path",
           "text": "extracted_text",
           "file_path": "file_path"
         }
       ]
     }
     ```

---

## Features and Functionalities

### Chatbot
- **Contextual Responses**: Uses embeddings and similarity calculations to provide meaningful answers.
- **Customizable Models**: Allows integration with different NLP models.

### PDF Handling
- **Upload PDFs**: Users can upload documents for analysis.
- **Metadata Extraction**: Retrieves title, author, and page count.
- **Content Retrieval**: Finds relevant sections based on user queries.

### Embedding Service
- **Text to Embedding**: Converts user queries and document chunks into embeddings for similarity comparison.
- **Device Management**: Automatically moves tensors to CPU for compatibility.

---

## Notes
- Ensure that the `uploads` directory is writable for storing uploaded files.

