import json

def extractor(input_file,output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Selon le moteur, les données peuvent être dans data["song"]["notes"]
    notes_sections = data["song"]["notes"]

    player1_notes = []
    player2_notes = []

    # Parcourir toutes les sections
    for section in notes_sections:
        must_hit = section.get("mustHitSection", False)
        section_notes = section.get("sectionNotes", [])

        for note in section_notes:
            # Certaines notes peuvent avoir 3 ou 4 valeurs (on garde les 3 premières)
            time = note[0]
            direction = note[1]
            sustain = note[2] if len(note) > 2 else 0

            if must_hit:
                player1_notes.append([time, direction, sustain])
            else:
                player2_notes.append([time, direction, sustain])

    # Écrire dans le fichier output.txt
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("player1 = [\n")
        for note in player1_notes:
            f.write(f"  {note},\n")
        f.write("]\n\n")

        f.write("player2 = [\n")
        for note in player2_notes:
            f.write(f"  {note},\n")
        f.write("]\n")

    print(f"Extraction terminée ! Résultat enregistré dans '{output_file}'.")

if __name__ == "__main__":
    extractor("data/soporific.json","output.txt")