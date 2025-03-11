#  Retrieve relevant documents based on user queries.
# 2️⃣ Use Falcon to generate responses based on retrieved context.

import faiss
import numpy as np
import boto3

# Load FAISS index
index = faiss.read_index("faiss_index.bin")

# User query
query = "What are the best headphones for travel?"
query_embedding = embedding_model.encode([query]).astype('float32')

# Search top-3 closest matches
D, I = index.search(query_embedding, k=3)
retrieved_docs = [docs[i] for i in I[0]]

# Construct prompt for Falcon
context = "\n".join(retrieved_docs)
prompt = f"Based on the following information, answer the user's query:\n{context}\n\nQuery: {query}"

# Call Falcon API
response = falcon_predictor.predict({
    "inputs": prompt,
    "parameters": {"max_new_tokens": 200}
})

print(response)
