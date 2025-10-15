import json

def extractor(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    notes_sections = data["song"]["notes"]

    player1_notes = []
    player2_notes = []

    for section in notes_sections:
        must_hit = section.get("mustHitSection", False)
        section_notes = section.get("sectionNotes", [])

        for note in section_notes:
            time = note[0]
            direction = note[1]
            sustain = note[2] if len(note) > 2 else 0

            if must_hit:
                if direction in [0, 1, 2, 3]:
                    player1_notes.append([time, direction, sustain])
                elif direction in [4, 5, 6, 7]:
                    player2_notes.append([time, direction - 4, sustain])
            else:
                if direction in [0, 1, 2, 3]:
                    player2_notes.append([time, direction, sustain])
                elif direction in [4, 5, 6, 7]:
                    player1_notes.append([time, direction - 4, sustain])

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
    extractor("data/soporific.json", "output.txt")
