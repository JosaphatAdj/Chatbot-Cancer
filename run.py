#!/usr/bin/env python3
"""
Point d'entrée alternative pour lancer l'application FastAPI
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",  # ⬅️ CHANGEMENT ICI : chaîne d'importation !
        host="0.0.0.0",
        port=8000,
        reload=True
    )