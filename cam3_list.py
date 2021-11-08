
# =========================================================================
# MAIN
# =========================================================================

# On déclare une liste, qui est vide au début
maListe = list()
# On peut écrire "maListe = []" à la place mais je trouve ça moins clair
# car on peut confondre avec d'autres types (ex: dictionnaire)

# On peut ajouter des éléments, qui garderont l'order dans lequels ils sont ajoutés
maListe.append("Ceci")
maListe.append("est")
maListe.append("une")
maListe.append("liste")
print("Une liste:", maListe)

# On peut modified un élément
# Le premier est 0, le deuxième 1, ...
maListe[2] = "MA"
print("Ma liste (modifier):", maListe)

# On peut insérer des éléments à n'importe quel endroit
maListe.insert(3, "superbe")
print("Superbe liste (insérer):", maListe)

# Retrouver un index directement par ce qu'il contient
idx = maListe.index("MA")
maListe[idx] = "THE"
print("THE liste (index):", maListe, " idx=", idx)

# On peut mixer les types (string, nombre, ...)
maListe.append("de") # chaine de caractères
maListe.append(2021) # entier
print("Liste mixée:", maListe)

# Boucler sur tous les éléments de la liste
for element in maListe:
    print("for:", element)

# Est-ce qu'un élément est dans la liste?
if "THE" in maListe:
    print("if: THE est dans ma liste")

# le dernier éléments porte l'index -1
print("Dernier             = ", maListe[-1])
print("Avant dernier       = ", maListe[-2])
print("Avant avant dernier = ", maListe[-3])

# longueur de la liste
print("Longueur = ", len(maListe))

# Retirer un élément
maListe.remove("superbe")
print("Remove: ", maListe)

# Il y a plein d'autres fonctions disponibles ...