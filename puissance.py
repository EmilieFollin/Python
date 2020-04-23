# coding: utf-8

 

# Class 1 (Jeu)
# Générer une nouvelle partie / Créer la grille / Effacer la grille / Préparer le premier tour / Test le placement est autorisé / Tester si la partie est finie (gagnée, perdue ou nulle)

 

# Class 2 (Player)
# Choisir l'emplacement du pion / Choix des couleurs des joueurs

 

# Class 2-1 (Joueur)
# ...

 

# Class 2-2 (Bot)
# Définir un niveau / Définir des stratégies / Jouer son tour / (Prévoir son coup à l'avance)

 


grille = [
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    ["-","-","-","-","-","-","-"],
    ["1","2","3","4","5","6","7"]
]

 

# choix 1
# join concatène des éléments de listes ensemble
# sous forme de string
# :2 est une marge entre chaque string (comme un padding en CSS)
# Cette fonction n'est pas de moi, c'est cadeau
# Difficile d'y intégrer une couleur de joueurs
# On se baserait sur des X et des O pour différencier les joueurs
# Comme au morpion
print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
      for row in grille]))

 

# choix 2
# On print chaque case, contrairement à la solution ci-dessus qui
# ne fait qu'un print. C'est moins performant, mais plus maléable.
# 31 = rouge, 33 = jaune
for row in grille:
    for value in row:
        print '{:4}'.format("\033[1;33;40m"+value),
    print