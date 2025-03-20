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
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")
pca = joblib.load("pca.pkl")

# Listes des colonnes à exclure
colonnes_a_exclure = set([
    '292', '157', '158', '293', '492', '220', '358', '85', '516', '517', '382', '111', '383', '384', '246', '244', '245', '110', '518', '109', '579', '581', '578', '580', '346', '72', '73', '345', '247', '385', '112', '519', '567', '563', '562', '569', '566', '565', '568', '564', '546', '548', '547', '554', '553', '552', '551', '550', '549', '556', '555', '557',
    '5', '13', '42', '49', '52', '69', '97', '141', '149', '178', '179', '186', '189', '190', '191', '192', '193', '194', '226', '229', '230', '231', '232', '233', '234', '235', '236', '237', '240', '241', '242', '243', '256', '257', '258', '259', '260', '261', '262', '263', '264', '265', '266', '276', '284', '313', '314', '315', '322', '325', '326', '327', '328', '329', '330', '364', '369', '370', '371', '372', '373', '374', '375', '378', '379', '380', '381', '394', '395', '396', '397', '398', '399', '400', '401', '402', '403', '404', '414', '422', '449', '450', '451', '458', '461', '462', '463', '464', '465', '466', '481', '498', '501', '502', '503', '504', '505', '506', '507', '508', '509', '512', '513', '514', '515', '528', '529', '530', '531', '532', '533', '534', '535', '536', '537', '538'
])

# Dictionnaire d'encodage des phases
encodage_phase = {
    'Dépôt de couches minces': 0,
    'Gravure': 1,
    'Implantation ionique': 2,
    'Lithographie': 3
}

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = data.get("features")

        if not features or len(features) != 125:
            return jsonify({"error": "Les données doivent contenir exactement 125 valeurs"}), 400

        # Conversion en DataFrame
        X_input = pd.DataFrame([features])

        # Suppression des colonnes non nécessaires
        X_input.drop(columns=[str(col) for col in colonnes_a_exclure if str(col) in X_input.columns], inplace=True)

        # Encodage de la dernière colonne (si présente)
        if isinstance(X_input.iloc[0, -1], str):
            X_input.iloc[0, -1] = encodage_phase.get(X_input.iloc[0, -1], -1)  # -1 en cas de valeur inconnue

        # Prétraitement des données
        X_scaled = scaler.transform(X_input)
        X_pca = pca.transform(X_scaled)

        # Prédiction
        prediction = model.predict(X_pca)

        return jsonify({"prediction": int(prediction[0])})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
