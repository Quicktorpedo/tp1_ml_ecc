import json
import random
from datetime import datetime, timedelta

# Dictionnaire d'encodage des phases
encodage_phase = {
    'Dépôt de couches minces': 0,
    'Gravure': 1,
    'Implantation ionique': 2,
    'Lithographie': 3,
    'Métallisation': 4,
    'Test électrique': 5
}

# Générer une date de départ aléatoire
start_date = datetime(2008, 7, 19, 11, 55, 0)

# Générer les données
# features = [start_date.strftime("%Y-%m-%d %H:%M:%S")]  # Valeur temporelle initiale
features = [round(random.uniform(0, 1250), 2) for _ in range(124)]  # 590 valeurs float64
features.append(random.choice(list(encodage_phase.keys())))  # Dernière valeur choisie aléatoirement

# Créer le dictionnaire JSON
data = {"features": features}

# Sauvegarder dans un fichier JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Fichier JSON 'data.json' généré avec succès !")
