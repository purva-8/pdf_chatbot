from sentence_transformers import SentenceTransformer
import numpy as np
import json
import os
from sklearn.metrics.pairwise import cosine_similarity

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate and Save embeddings 
def generate_and_save_embeddings(pdf_id, extracted_text):
    text_lines = extracted_text.split("\n")
    embeddings = embedding_model.encode(text_lines, convert_to_tensor=False)  # Get a 2D array

    embeddings_path = f'embeddings/{pdf_id}_embeddings.json'
    with open(embeddings_path, "w") as f:
        json.dump([embedding.tolist() for embedding in embeddings], f)
    
    return embeddings_path

# Compute the similarity 
def compute_similarity(question_embedding, pdf_embeddings):
    similarities = cosine_similarity(question_embedding.reshape(1, -1), pdf_embeddings)
    return similarities
