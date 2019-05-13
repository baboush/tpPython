from random import randrange
from math import ceil


continu = True
solde = 1000

while continu:
    print("Votre solde est de : " ,solde, "\n")
    print("Pour quitter le programme taper 'q'\n")
    quitter = input("Voulez vous jouer ?\n")
    if quitter == "q":
        print ("Etes-vous sur de vouloir quitter le jeux ?\n")
        choix = input("Taper 'o' pour oui 'n' pour non ")
        if choix == "o":
            exit()
    elif solde == 0:
        print("Le jeux est terminé !!")
        exit()
    else:
        print("le jeux commence")
    while True:
        mise = input("Entrer une mise : ")
        try:
            mise = int(mise)
            assert mise >= 0
            if mise > solde:
                raise ValueError("Solde insuffisant\n")
        except ValueError:
            print("Votre solde n'est pas suffisante\n")
        except AssertionError:
            print("votre mise est égale a 0 ou negative\n")
        else:
            break
    solde = solde - mise
    while True:
        numUser = input("Choisissez un numero entre 0 et 50 : ")
        try:
            numUser = int(numUser)
            assert ((numUser >= 0) and (numUser <= 49))
            if numUser != int(numUser):
                raise ValueError("Vous n'avez pas entré un nombre !\n")
            else:
                num = randrange(50)
                if mise == num:
                    print("bravo vous avez gagné : ", mise * 3)
                    gains = mise * 3
                    solde = solde + gains
                elif (mise != num):
                    if ((mise % 2 == 0) and (num % 2 == 0)):
                        print("Vous avez gagné : ", mise * 1.5)
                        gains = ceil(mise*1.5)
                        solde = solde + gains
                    elif ((mise % 2 != 0) and (mise % 2 != 0)):
                         print("Vous avez gagné : ", mise * 1.5)
                         gains = ceil(mise*1.5)
                         solde = solde + gains
                    else:
                        print("Vous avez perdu !")
        except ValueError:
            print("Veuillez entrer un nombre\n")
        except AssertionError:
            print("La valeur entrée n'est pas comprise entre 0 et 50\n")
        else:
            break











