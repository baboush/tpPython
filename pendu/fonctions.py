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


def randomMot(liste, mot_cache):
    mot = random.choice(donnees.MOTS)  # selection mot au hasard
    liste = [i for i in mot]
    index = 0
    mot_cache = []
    while index < len(liste):  # cache le mot
        mot_cache.append('*')
        index += 1
    mot_decouvert = ''.join(liste)
    mot_etoile = ''.join(mot_cache)
    return mot_decouvert, mot_etoile


def trouverMot(mot_decouvert, mot_etoile):
    mot_decouvert_split = mot_decouvert
    mot_etoile_split = [i for i in mot_etoile]
    i = donnees.NBR_CHANCES
    while i > 0:
        lettre_user = str(input("Entrée une lettre : "))
        index = 0
        while index < len(mot_decouvert_split):
            if lettre_user == mot_decouvert_split[index]:
                print("vous avez trouver une lettre")
                mot_etoile_split[index] = lettre_user
            index += 1
        mot_etoile = "".join(mot_etoile_split)
        print(mot_etoile)
        if mot_etoile == mot_decouvert_split:
            print("vous avez trouvé le mot")
            return i
        i -= 1
