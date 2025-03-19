import os
import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Initialisation de l'application Flask
app = Flask(__name__)

# Chargement du modèle et des objets de prétraitement
model = joblib.load("best_model.pkl")  # Assurez-vous que ce fichier existe dans le même dossier
scaler = joblib.load("scaler.pkl")  # Fichier contenant le StandardScaler
pca = joblib.load("pca.pkl")  # Fichier contenant le modèle PCA

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupération des données envoyées par l'utilisateur
        data = request.get_json()
        features = data.get("features")

        # if not features or len(features) != 591:
        #     return jsonify({"error": "Les données doivent contenir exactement 591 valeurs"}), 400

        # Conversion en DataFrame et application du prétraitement
        X_input = pd.DataFrame([features])
        X_scaled = scaler.transform(X_input)
        X_pca = pca.transform(X_scaled)

        # Prédiction avec le modèle chargé
        prediction = model.predict(X_pca)

        return jsonify({"prediction": int(prediction[0])})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
