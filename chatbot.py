import os
import pickle
import faiss
import numpy as np

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

from google import genai

# -----------------------------------
# Load API Key
# -----------------------------------

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# -----------------------------------
# Load Embedding Model
# -----------------------------------

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# -----------------------------------
# Load FAISS
# -----------------------------------

index = faiss.read_index(
    "vectorstore/index.faiss"
)

with open(
    "vectorstore/chunks.pkl",
    "rb"
) as f:
    chunks = pickle.load(f)

# -----------------------------------
# Ask Question
# -----------------------------------

def ask_question(question):

    query_embedding = embedding_model.encode(
        [question]
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        3
    )

    context = ""

    for idx in indices[0]:
        context += chunks[idx] + "\n\n"

    prompt = f"""
You are an AI assistant.

Answer ONLY using the context below.

Context:

{context}

Question:

{question}
"""

    response = client.models.generate_content(
    model="models/gemini-flash-latest",
    contents=prompt
    )

    return response.text