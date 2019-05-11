from random import randrange
from math import ceil

print("Bienvenu dans le jeu de casino")
print("Voulez vous jouer ? o/n")
continu = True
while continu:
    choix = input("Tapez <o> pour commencer une partie, tapez <n> pour"+
        " quitter : ")
    try:
        choix = str(choix)
        if ((choix != "n") or (choix != "o")):
            raise ValueError
    except ValueError:
        if ((choix == "o" or choix == "n")):
                pass
        else:
            print("Vous avez entré(e) un nombre ou une commande erronée")
    if choix == "n":
        continu = False
        print("Vous avez quitter la partie")
        exit()



