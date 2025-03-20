import requests
import json

url = "http://127.0.0.1:5000/predict"

# Charger les données JSON générées
with open("data.json", "r") as f:
    data = json.load(f)

# Vérifier que nous avons 591 valeurs
if "features" in data and len(data["features"]) == 125:
    response = requests.post(url, json=data)  # ✅ Envoi correct du JSON
    print(response.json())
else:
    print("Erreur : Le JSON doit contenir exactement 125 valeurs.")