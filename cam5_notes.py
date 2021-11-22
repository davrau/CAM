
# =========================================================================
# MAIN
# =========================================================================

# matières
matieres = ["Maths", "Francais", "Anglais", "Espagnol"]

# On déclare un dictionnaire
notes = dict()

notes["Maths"] = [14.5, 15.3, 12.0]
notes["Francais"] = [16.0]
notes["Anglais"] = [16.0, 20.0]
notes["Espagnol"] = [13.33, 14.0]

notes["Espagnol"].append(12.0)

# Liste ordonnée des matières (le dico n'est pas ordonné)
for matiere in matieres:
    print(matiere)
    for note in notes[matiere]:
        print("    ", note)

# Affichage "brut" du dico {x1 : y1, x2 : y2, ...}.
# Les clés du tableau sont les noms des matières
# Les valeurs y1, y2, ... sont ici des listes de notes
print(notes)