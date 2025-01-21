from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
from sentence_transformers import SentenceTransformer

# Load the model for sentence embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Finding the most relevant text based on similarity
def find_most_relevant_text(question, pdf_data):
    try:
        # Encode the user's question into an embedding
        question_embedding = model.encode([question], convert_to_tensor=True)

        # Load the PDF embeddings (ensure file exists and is valid)
        with open(pdf_data["embeddings_path"], "r") as f:
            pdf_embeddings = np.array(json.load(f))

        # Cosine Similarity 
        similarities = cosine_similarity(question_embedding.reshape(1, -1), pdf_embeddings)
        most_relevant_index = similarities.argmax()

        # Retrieve the relevant context 
        lines = pdf_data["text"].split("\n")
        context_window = 3  # Number of lines to consider before and after
        start_index = max(0, most_relevant_index - context_window)
        end_index = min(len(lines), most_relevant_index + context_window + 1)

        # Return the context as the most relevant text
        return "\n".join(lines[start_index:end_index])
    
    except Exception as e:
        return f"Error finding relevant text: {e}"
