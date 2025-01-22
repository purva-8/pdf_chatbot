from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

#Chunk PDF text into smaller pieces
def chunk_pdf_text(pdf_text, chunk_size=500):
    return [pdf_text[i:i+chunk_size] for i in range(0, len(pdf_text), chunk_size)]

# Retrieve the most relevant chunk
def retrieve_with_tfidf(question, chunks):
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(chunks)
    question_vec = vectorizer.transform([question])
    similarities = (tfidf_matrix * question_vec.T).toarray()
    best_chunk_idx = np.argmax(similarities)
    return chunks[best_chunk_idx]
