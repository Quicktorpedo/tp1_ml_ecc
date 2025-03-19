import json
import random

# Générer 591 valeurs aléatoires entre 0 et 1250
features = [round(random.uniform(0, 1250), 2) for _ in range(125)]

# Créer le dictionnaire JSON
data = {"features": features}

# Sauvegarder dans un fichier JSON
with open("data_125.json", "w") as f:
    json.dump(data, f, indent=4)

print("Fichier JSON 'data.json' généré avec succès !")
