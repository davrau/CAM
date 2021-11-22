
# =========================================================================
# MAIN
# =========================================================================

# On déclare un dictionnaire
moyenne = dict()

moyenne["Maths"] = 14.5
moyenne["Francais"] = 16.0
moyenne["Anglais"] = 16.0
moyenne["Espagnol"] = 13.33

print(moyenne["Francais"])
print(moyenne)

# boucle sur les clés du dico (Francais, Maths, ...) pas dans l'ordre
for k in moyenne.keys():
    print("for", k, moyenne[k])
