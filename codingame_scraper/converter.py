import os
import re
import csv
import json
from pathlib import Path
from datetime import datetime

k_Level = "expert"
k_JSON_In = f"{k_Level}.json"

os.chdir(Path(__file__).parent)

with open(k_JSON_In, "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Si le JSON est une liste, prendre le premier élément
if isinstance(data, list) and len(data) > 0:
    data = data[0]

# Extraire les puzzles
puzzles = data.get("puzzles_data", [])

current_date = datetime.now().strftime("%Y%m%d")
csv_filename = f"{k_Level}_{current_date}.csv"


# Extraire le nb de participants
def extract_participants(text):
    # Remplacer l'espace insécable (\u00A0) par un espace normal
    text = text.replace("\u00A0", " ")

    match = re.search(r"(\d[\d\s]*)", text)
    if match:
        # Supprimer les espaces dans le nombre trouvé (ex: "1 080" devient "1080")
        return match.group(1).replace(" ", "")
    return "0"


with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["titre", "nombre de participants"])
    for puzzle in puzzles:
        title = puzzle.get("title", "No Title")
        participants_text = puzzle.get("participants", "Unknown")
        participants = extract_participants(participants_text)
        csv_writer.writerow([title, participants])
print(f"Done : {csv_filename}")
