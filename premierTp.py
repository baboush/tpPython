anneeEntrer = int(input("entrer une année : "))

if anneeEntrer % 4 != 0:
    print("Votre année n'est pas bissextile")
elif anneeEntrer % 100 == 0:
    if anneeEntrer % 400 == 0:
        print("Votre année est bissextile")
    else:
        print("Votre année n'est pas bissextile")
else:
    print ("votre année est bissextile")


