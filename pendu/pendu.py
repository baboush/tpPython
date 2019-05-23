"""main pendu"""
import fonctions as f
import donnees

mot_cache = ""
mot_decouvert = ""
mot_étoile = ""
nom = ""
score = 0
score_a_ajouter = 0
i = 0

f.creerFichier()
f.lireFichier()
nom, score = f.lireJoueur(nom, score)
mot_decouvert, mot_etoile = f.randomMot(donnees.MOTS, mot_cache)
f.trouverMot(mot_decouvert, mot_etoile, nom)
f.enregistrerJoueur()
