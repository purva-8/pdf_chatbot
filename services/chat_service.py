import google.generativeai as genai
from utils.similarity_utils import find_most_relevant_text

# Generate a response using Google Gemini API
def generate_chat_response(question, pdf_data):
    try:
        # Extract the relevant context from the PDF
        context = find_most_relevant_text(question, pdf_data)
        
        # Define the prompt for the AI model
        prompt = f"Give the answer from the provided context and not any data outside the context. Context:\n{context}\n\nQuestion: {question}\n\nAnswer:"
        
        # Interact with Google Gemini API
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        
        # Return the response text, or a fallback message if the response is empty
        if response and response.text.strip():
            return response.text.strip()
        else:
            return "Sorry, I couldn't find an answer. Please try asking another question."

    except Exception as e:
        return f"Error generating response: {e}"
