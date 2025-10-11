# 🏥 Chatbot Expert - Cancer du Sein (Bénin/Afrique)

**Système RAG intelligent pour la sensibilisation et la lutte contre le cancer du sein**  
*Déploiement Render avec FastAPI*

---

## 🌟 Fonctionnalités

- **🤖 Réponses expertes** basées sur la documentation médicale
- **🌍 Contexte adapté** au Bénin et à l'Afrique
- **🔍 Recherche RAG** dans une base de documents spécialisés
- **⚡ API RESTful** pour intégration facile
- **💬 Historique contextuel** intégré dans chaque requête

---

## 🚀 Déploiement sur Render

### Prérequis
- Compte [Render](https://render.com/)
- Dossier `rag_artifacts` contenant :
  - Base vectorielle ChromaDB
  - Documents indexés sur le cancer du sein
  - Configuration du système

### Étapes de Déploiement

1. **📦 Préparer les fichiers**
   ```bash
   chatbot-render/
   ├── app/
   │   ├── main.py
   │   ├── rag_system.py
   │   ├── requirements.txt
   │   ├── start.sh
   │   └── render.yaml
   ├── rag_artifacts/
   └── README.md