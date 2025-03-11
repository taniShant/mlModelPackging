# Prepare Document Indexing with FAISS 
# convert text data into embeddings using a transformer model like all-MiniLM-L6-v2
######################
# FAISS (Facebook AI Similarity Search) is an open-source library developed by Meta (formerly Facebook) for 
# efficient similarity search and clustering of dense vectors. It is commonly used for nearest neighbor search, 
# especially in high-dimensional spaces, making it ideal for applications like:
# Large-scale vector search (e.g., finding similar items in a recommendation system)
# Retrieval-augmented generation (RAG) (e.g., searching a knowledge base for LLMs)
# Image and text similarity matching 
# K-Nearest Neighbors (KNN) acceleration
######################
# Why Use FAISS?
# Fast & Scalable: Can handle millions to billions of vectors efficiently.
# GPU Acceleration: Supports CUDA for high-performance search.
# Indexing Strategies: Various indexing methods (IVF, HNSW, PQ, etc.) balance speed vs. accuracy.
# Optimized for High-Dimensional Data: Works well with embeddings from models like OpenAI, BERT, or CLIP.

from sentence_transformers import SentenceTransformer
import faiss, boto3 
import numpy as np

# Load embedding model
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Example documents
docs = [
    "The best running shoes for marathon training",
    "High-performance laptops for software development",
    "Top noise-canceling headphones under $200"
]

# Convert to embeddings
embeddings = embedding_model.encode(docs)
embeddings = np.array(embeddings).astype('float32')

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Save FAISS index
faiss.write_index(index, "faiss_index.bin")

#Upload faiss_index.bin to S3 so it can be loaded dynamically.
# Upload to S3
s3 = boto3.client('s3')
s3.upload_file("faiss_index.bin", "your-bucket-name", "faiss_index.bin")

print("✅ FAISS index updated!")