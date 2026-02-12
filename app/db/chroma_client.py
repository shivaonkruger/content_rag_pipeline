import chromadb
from chromadb.config import Settings
from app.config import CHROMA_DB_DIR, COLLECTION_NAME

client = chromadb.Client(
    Settings(
        persist_directory=CHROMA_DB_DIR,
        anonymized_telemetry=False
    )
)

collection = client.get_or_create_collection(name=COLLECTION_NAME)
