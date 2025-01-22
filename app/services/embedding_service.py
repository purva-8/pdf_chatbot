from sentence_transformers import SentenceTransformer
import numpy as np
import json
import os
from sklearn.metrics.pairwise import cosine_similarity

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

#Generate and save embeddings for the PDF text
def generate_and_save_embeddings(pdf_id, extracted_text):
    text_lines = extracted_text.split("\n")
    embeddings = embedding_model.encode(text_lines, convert_to_tensor=True).to('cpu').numpy()  # Get a 2D array

    embeddings_path = f'../data/embeddings/{pdf_id}_embeddings.json'
    with open(embeddings_path, "w") as f:
        json.dump([embedding.tolist() for embedding in embeddings], f)
    
    return embeddings_path

# Cosine similarity
def compute_similarity(question_embedding, pdf_embeddings):
    similarities = cosine_similarity(question_embedding.reshape(1, -1), pdf_embeddings)
    return similarities
