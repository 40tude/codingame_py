ArrayOfMountains = []                                               # tableau dynamique
while True:
    for i in range(8):
        ArrayOfMountains.append(int(input()))                       # range l'entrée convertie en entier
    
    IndexOfMax = ArrayOfMountains.index(max(ArrayOfMountains))      # recherche l'indice du max
    print(IndexOfMax)                                               # affiche l'indice en question
    del ArrayOfMountains[:]                                         # supprime le tableau car on va en reconstruire un au prochaine tour
