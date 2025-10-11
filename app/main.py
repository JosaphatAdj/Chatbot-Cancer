from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag_system import CancerSeinRAG
import os
import time
import logging

# Configuration logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Chatbot Cancer du Sein",
    description="Système RAG expert en cancer du sein pour le Bénin/Afrique",
    version="1.0.0"
)

# CORS pour le frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modèle pour la requête
class QuestionRequest(BaseModel):
    question: str

# Modèle pour la réponse
class AnswerResponse(BaseModel):
    answer: str
    response_time: float
    status: str

# Initialisation du système RAG
@app.on_event("startup")
async def startup_event():
    logger.info("🔄 Démarrage du système RAG...")
    global rag_system
    try:
        rag_system = CancerSeinRAG()
        logger.info("✅ Système RAG initialisé avec succès")
    except Exception as e:
        logger.error(f"❌ Erreur initialisation RAG: {e}")
        raise e

# Endpoint santé
@app.get("/")
async def root():
    return {
        "status": "online", 
        "service": "Chatbot Cancer du Sein",
        "version": "1.0.0"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

# Endpoint principal - RAG
@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    start_time = time.time()
    
    try:
        logger.info(f"📥 Question reçue: {request.question[:50]}...")
        
        # Appel au système RAG
        response = rag_system.query(request.question)
        response_time = time.time() - start_time
        
        logger.info(f"✅ Réponse générée en {response_time:.2f}s")
        
        return AnswerResponse(
            answer=response,
            response_time=response_time,
            status="success"
        )
        
    except Exception as e:
        response_time = time.time() - start_time
        logger.error(f"❌ Erreur traitement: {e}")
        
        return AnswerResponse(
            answer="Désolé, une erreur s'est produite. Veuillez réessayer.",
            response_time=response_time,
            status="error"
        )

