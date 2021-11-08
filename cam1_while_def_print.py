# =========================================================================
# Calcule 2 à la puissance n
# =========================================================================

# Définition d'une fonction qui retourne une valeur
# le "def" finit par un ":"
# La fonction accepte un paramètre "n". On retour "2^n" (ex: 2 à la puissance n, ex 2^3=8)
def DeuxPuissanceN(n):

    # Création de la variable locale "res" que l'on initialise à 1
    res = 1

    # Tant que "n" est positif on exécute la boucle "while" (ex: 3, 2, 1)
    while n > 0:
        # On multiplie res par 2 (ce qui calcule 2 à la puissance "n")
        res = res * 2
        # décrémenter "n" pour quitter la boucle quand n==0
        n = n - 1
    
    # Retourner la valeur du résultat "res"
    return(res)

# =========================================================================
# MAIN
# =========================================================================

# Première ligne exécutée par le programme
print("Début du programme")

n1 = 3
n2 = 4

# On fait un print du résultat de la fonction
# La fonction est appelée AVANT le print pour calculer le résultat
print("2^%d vaut %d" % (n1, DeuxPuissanceN(n1)))

# Deuxième appel avec "n2"
# C'est l'intérêt d'avoir une fonction pour faire plusieurs fois un calcul
print("2^%d vaut %d" % (n2, DeuxPuissanceN(n2)))

print("Fin du programme")
