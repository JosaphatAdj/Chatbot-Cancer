import os
import chromadb
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import logging

logger = logging.getLogger(__name__)

class CancerSeinRAG:
    def __init__(self):
        self.embed_model = None
        self.index = None
        self.query_engine = None
        self._initialize_rag()
    
    def _initialize_rag(self):
        """Initialise le système RAG avec les artifacts"""
        try:
            logger.info("🔧 Initialisation du système RAG...")
            
            # Configuration embeddings
            self.embed_model = HuggingFaceEmbedding(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )
            logger.info("✅ Embeddings initialisés")
            
            # Chargement base vectorielle
            chroma_path = os.path.join(os.getcwd(), "rag_artifacts", "chroma_db")
            chroma_client = chromadb.PersistentClient(path=chroma_path)
            chroma_collection = chroma_client.get_collection("sein_awareness_rag")
            vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
            storage_context = StorageContext.from_defaults(vector_store=vector_store)
            
            # Création index
            self.index = VectorStoreIndex.from_vector_store(
                vector_store, 
                storage_context=storage_context, 
                embed_model=self.embed_model
            )
            logger.info("✅ Index vectoriel chargé")
            
            # Configuration moteur de requête
            self.query_engine = self.index.as_query_engine(
                similarity_top_k=3,
                response_mode="compact"
            )
            logger.info("✅ Moteur de requête configuré")
            
        except Exception as e:
            logger.error(f"❌ Erreur initialisation RAG: {e}")
            raise e
    
    def query(self, question: str) -> str:
        """Exécute une requête RAG"""
        if self.query_engine is None:
            raise Exception("Système RAG non initialisé")
        
        try:
            response = self.query_engine.query(question)
            return str(response)
        except Exception as e:
            logger.error(f"❌ Erreur lors de la requête: {e}")
            raise e