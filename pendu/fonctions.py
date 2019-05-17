"""fonction du jeux du pendu"""

import os
import donnees
import pickle

def creerFichier():
    if os.path.isfile("scores.txt") == False:
        print("le fichier des scores n'existe pas")
        print("creation du fichier scores")
        fichier = open("scores.txt", "x")
        fichier.close()
    else:
        print("Un fichier scores à été trouvé")
        pass

def lireFichier():
    try:
        with open("scores.txt", "rb") as fichier:
            lecture_fichier = pickle.load(fichier)
            print(lecture_fichier)
        fichier.close()
    except EOFError:
        print("le fichier est vide")
        pass
    
def enregistrerJoueur(nom):
    with open("scores.txt", "ab") as fichier:
        ecriture = pickle.dump(nom, fichier)
    fichier.close()

