rag-gemini-chroma/
│
├── app/
│   ├── main.py                # FastAPI server entry
│   ├── config.py              # env + settings
│   ├── rag_pipeline.py        # embedding + retrieval + generation
│   ├── db/
│   │   └── chroma_client.py   # chromadb init + collection
│   └── schemas.py             # request/response models
│
├── .env
├── requirements.txt
└── README.md
