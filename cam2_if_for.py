
# =========================================================================
# MAIN
# =========================================================================

# Pour toutes les valeurs de 0 à 9
# Le "for" finit par un ":"
for valeur in range(10):

    # Si le reste de la division par 2 est 0 alors la valeur est paire
    # Le "if" est dans la boucle "for" et finit par un ":"
    if valeur % 2 == 0:
        print("%d est pair" % (valeur))

    # Sinon elle est impaire (reste de la divsion par 2 vaut 1)
    # Le "else" est aligné avec le "if" et finit par un ":"
    else:
        print("%d est impair" % (valeur))
