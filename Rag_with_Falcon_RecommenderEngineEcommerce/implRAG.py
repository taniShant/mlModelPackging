#  Retrieve relevant documents based on user queries.
# Use Falcon to generate responses based on retrieved context.

import faiss
import numpy as np
import boto3
from sentence_transformers import SentenceTransformer
 
# Load embedding model (same one used in training)
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Load FAISS index from S3
s3 = boto3.client('s3')
s3.download_file("test-s3-asvectstr-eu-west-1", "faiss_index.bin", "faiss_index.bin")
index = faiss.read_index("faiss_index.bin")

#This query comes from frontend (client or Api )
def retrieve_similar_products(query):
    """Convert query to embedding and retrieve top products."""
    query_embedding = embedding_model.encode([query]).astype("float32")
    _, indices = index.search(query_embedding, k=5)  # Retrieve top 5 matches
    return indices

# User query


query = "What are the best headphones for travel?"

# query_embedding = embedding_model.encode([query]).astype('float32')

# # Search top-3 closest matches
# D, I = index.search(query_embedding, k=3)
# retrieved_docs = [docs[i] for i in I[0]]

# Construct prompt for Falcon
context = "\n".join(retrieved_docs)
prompt = f"Based on the following information, answer the user's query:\n{context}\n\nQuery: {query}"

# Call Falcon API
response = falcon_predictor.predict({
    "inputs": prompt,
    "parameters": {"max_new_tokens": 200}
})

print(response)
