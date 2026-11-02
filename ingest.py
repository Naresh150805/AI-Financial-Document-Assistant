import os
import pickle
import numpy as np
import faiss

from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

# --------------------------
# Read PDF
# --------------------------

reader = PdfReader("data/Naresh_S_Resume.pdf")

text = ""

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text + "\n"

print("PDF Loaded")

# --------------------------
# Split into chunks
# --------------------------

chunk_size = 500

chunks = [
    text[i:i+chunk_size]
    for i in range(0, len(text), chunk_size)
]

print("Chunks:", len(chunks))

# --------------------------
# Load embedding model
# --------------------------

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# --------------------------
# Create embeddings
# --------------------------

embeddings = model.encode(chunks)

embeddings = np.array(embeddings).astype("float32")

# --------------------------
# Build FAISS
# --------------------------

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# --------------------------
# Save FAISS
# --------------------------

os.makedirs("vectorstore", exist_ok=True)

faiss.write_index(
    index,
    "vectorstore/index.faiss"
)

with open(
    "vectorstore/chunks.pkl",
    "wb"
) as f:

    pickle.dump(chunks, f)

print("Vector Store Created Successfully")