"""fonction du jeux du pendu"""

import donnees
from random import choices
import pickle

"""on crée le fichier score si il existe pas
on lit et ajoute dans une bibliotheque"""
def fichier(JOUEURS):
    fichier = open("scores.txt", "rb")
    liste_joueur = pickle.Unpickler(fichier)
    JOUEURS = liste_joueur
    fichier.close()

"""on test si le joueur existe ou pas"""
def nomJoueur(nom, JOUEURS):
    for nom in JOUEURS.keys():
        if nom is not JOUEURS.keys():
            JOUEURS[nom] = 0
        else:
            print("Vous avez selectioné le joueur {}, votre score est de : {}"\
                  .format(JOUEURS.keys(), JOUEURS.values()))

def choixMots(MOTS):
    mot_Trouver = choices(MOTS)
    print("Le mot a trouver est de {} lettres".format(len(mot_Trouver)))
    return mot_Trouver

"""on ajoute le score au joueur
on l'enregistre dans le fichier"""
def ajoutScores(JOUEURS):
    JOUEURS[nom] = JOUEURS.values() + NBR_CHANCES
    with open("scores.txt", "wb") as fichier:
        save = pickle.Pickler(fichier)
        save.dump(JOUEURS)
    fichier.close()



