import uuid
import google.generativeai as genai
from app.config import GEMINI_API_KEY, EMBED_MODEL, GEN_MODEL
from app.db.chroma_client import collection

genai.configure(api_key=GEMINI_API_KEY)


def generate_embedding(text: str):
    response = genai.embed_content(
        model=EMBED_MODEL,
        content=text
    )
    return response["embedding"]


def store_content(text: str, metadata: dict = None):
    embedding = generate_embedding(text)

    collection.add(
        ids=[str(uuid.uuid4())],
        embeddings=[embedding],
        documents=[text],
        metadatas=[metadata or {}]
    )


def retrieve_context(query: str, k: int = 4):
    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    docs = results.get("documents", [[]])[0]
    return docs


def generate_answer(query: str):
    context_docs = retrieve_context(query)
    context = "\n".join(context_docs)

    prompt = f"""
You are a knowledge assistant.

Use ONLY the context below to answer.

Context:
{context}

Question:
{query}
"""

    model = genai.GenerativeModel(GEN_MODEL)
    response = model.generate_content(prompt)

    return response.text
