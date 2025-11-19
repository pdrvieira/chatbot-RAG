from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db

app = FastAPI(title="Petshop RAG API", version="1.0.0")

# configura CORS pro frontend conseguir chamar a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def inicio():
    return {"message": "Petshop RAG API está rodando"}


@app.get("/health")
def health():
    return {"status": "ok"}

