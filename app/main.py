from fastapi import FastAPI
from app.schemas import ContentRequest, QueryRequest, QueryResponse
from app.rag_pipeline import store_content, generate_answer

app = FastAPI(title="Gemini + Chroma RAG API")


@app.post("/content")
def ingest_content(payload: ContentRequest):
    store_content(payload.text, payload.metadata)
    return {"status": "stored"}


@app.post("/query", response_model=QueryResponse)
def query_rag(payload: QueryRequest):
    answer = generate_answer(payload.query)
    return QueryResponse(answer=answer)
