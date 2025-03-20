# Utilisation d'une image Python légère
FROM python:3.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier uniquement les dépendances pour optimiser le cache Docker
COPY requirements.txt requirements.txt

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier les dossiers nécessaires pour le projet
COPY api/ api/
COPY models/ models/
COPY data.json .
COPY image*.png .  # Inclure les images (si ton app les utilise)

# Exposer le port utilisé par ton application (ajuste si nécessaire)
EXPOSE 5000

# Démarrage de l'application
CMD ["python", "api/app.py"]
