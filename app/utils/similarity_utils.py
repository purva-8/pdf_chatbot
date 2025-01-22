from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from services.retrieval_service import chunk_pdf_text, retrieve_with_tfidf
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def find_most_relevant_text(question, pdf_data):
    try:
        # Chunk the PDF text
        pdf_text = pdf_data["text"]
        chunks = chunk_pdf_text(pdf_text)

        # Retrieve the best chunk
        relevant_chunk = retrieve_with_tfidf(question, chunks)

        # Encode question and chunk embeddings
        question_embedding = model.encode([question], convert_to_tensor=True).to('cpu').numpy()
        chunk_embeddings = model.encode(relevant_chunk, convert_to_tensor=True).to('cpu').numpy()

        #Refine context using embeddings
        similarities = cosine_similarity(question_embedding.reshape(1, -1), chunk_embeddings.reshape(1, -1))
        best_chunk_idx = np.argmax(similarities)
        return chunks[best_chunk_idx]
    except Exception as e:
        return f"Error finding relevant text: {e}"
