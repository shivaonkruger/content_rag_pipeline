from pydantic import BaseModel

class ContentRequest(BaseModel):
    text: str
    metadata: dict | None = None


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    answer: str
