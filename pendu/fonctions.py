"""fonction du jeux du pendu"""
import os
import pickle
import random
import donnees


def creerFichier():
    if os.path.isfile("scores.txt"):  # regarde si le fichier existe
        print("Un fichier scores à été trouvé")
        pass
    else:  # on crée le fichier s'il existe pas
        print("le fichier des scores n'existe pas")
        print("creation du fichier scores")
        fichier = open("scores.txt", "x")
        fichier.close()


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
        print(ecriture)
    fichier.close()


def randomMot():
    mot = random.choice(donnees.MOTS)  # selection mot au hasard
    liste = [i for i in mot]
    index = 0
    mot_cache = []
    while index < len(liste):  # cache le mot
        mot_cache.append('*')
        index += 1
    return liste, mot_cache
