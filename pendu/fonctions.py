"""fonction du jeux du pendu"""

import os
import donnees


def creerFichier():
    if os.path.isfile("scores.txt") == False:
        print("le fichier des scores n'existe pas")
        print("creation du fichier scores")
        fichier = open("scores.txt", "x")
        fichier.close()
    else:
        print("Un ichier scores à été trouvé")
        pass

