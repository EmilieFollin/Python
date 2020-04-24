# coding: utf-8

# Class 1 (Jeu)
# Prompts pour demander à l'utilisateur : mode de jeu, quelle couleur, tu joues quoi, etc.
# Générer une nouvelle partie / Créer la grille / Effacer la grille / Préparer le premier tour /
# Test le placement est autorisé / Tester si la partie est finie (gagnée, perdue ou nulle)

# Class 2 (Player)
# Choisir l'emplacement du pion / Choix des couleurs des joueurs

# Class 2-1 (Joueur)
# ...

# Class 2-2 (Bot)
# Définir un niveau / Définir des stratégies / Jouer son tour / (Prévoir son coup à l'avance)

# MENU de choix de JEU - 1vs1 <========== A FAIRE EN PROCEDURAL
# Système de tour <========== A FAIRE EN PROCEDURAL
### Définition de "à qui l'tour"
### Pouvoir placer un jeton/pion
###### Vérification d'une ligne de 4 (horizontal, vertical ou diagonal)
###### Si pas de victoire, alors on change de joueur pour le prochain coup
###### Si victoire
######### On pourrait compter le nombre de coup qui a été joué
######### On affiche quel joueur a gagné
######### On demande si le joueur veut rejouer
############ Si non, on quitte. Si oui, on relance la grille (ou le menu de choix)
# Grille
### Afficher la matrice 2 dimension (X,Y) (génération grille vide) <===
### Tenter d'ajouter des numéros de lignes/colonnes
### Update de la grille à chaque coup joué + couleur adéquate <===

# MENU de choix de JEU - 1vsCPU
# Système de tour
### Définition de "a qui l'tour"
### Pouvoir placer un jeton/pion
###### Si c'est au CPU de jouer
######### Il joue son coup en prenant en considération :
############ Analyse de la grille (où l'opposant en est ? où j'en suis ?)
############ Son niveau (easy, normal, hard)
############ Son profil (Agressif, Passif...)
###### Vérification d'une ligne de 4 (horizontal, vertical ou diagonal)
###### Si pas de victoire, alors on change de joueur pour le prochain coup
###### Si victoire
######### On pourrait compter le nombre de coup qui a été joué
######### On affiche quel joueur a gagné
######### On demande si le joueur veut rejouer
############ Si non, on quitte. Si oui, on relance la grille (ou le menu de choix)
# Grille
### Afficher la matrice 2 dimension (X,Y) (génération grille vide)
### Tenter d'ajouter des numéros de lignes/colonnes
### Update de la grille à chaque coup joué + couleur adéquate

# MENU de choix de JEU - CPUvsCPU
# IDENTIQUE a 1vsCPU sauf que la couche du joueur est remplacé par un deuxième bot

grille = [
	[" "," "," "," "," "," "," "], #0
	[" "," "," "," "," "," "," "], #1
	[" "," "," "," "," "," "," "], #2
	[" "," "," "," "," "," "," "], #3
	[" "," "," "," "," "," "," "], #4
	[" "," ","O"," "," "," "," "], #5
	["-","-","-","-","-","-","-"],
	["1","2","3","4","5","6","7"]
	 #0  #1  #2  #3  #4  #5  #6 <idx^
]

# choix 1
# join concatène des éléments de listes ensemble
# sous forme de string
# :2 est une marge entre chaque string (comme un padding en CSS)
# Cette fonction n'est pas de moi, c'est cadeau
# Difficile d'y intégrer une couleur de joueurs
# On se baserait sur des X et des O pour différencier les joueurs
# Comme au morpion
# print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
#      for row in grille]))

# choix 2
# On print chaque case, contrairement à la solution ci-dessus qui
# ne fait qu'un print. C'est moins performant, mais plus maléable.
# 31 = rouge, 33 = jaune
# for row in grille:
#    for value in row:
#        print '{:4}'.format("\033[1;33;40m"+value),
#    print







# @description : This function loop in array and concatenate strings
# with tab's value by index to format menu -> user friendly
# @return : <str>
def concatLoopArray(tab, message):
	i = 1
	for mode in tab:
		message += "\n" + str(i) + "- " + tab[i-1]
		i += 1
	return message

# @description : This function shows the first message of the game and gives the
# possibility to the user to choose a game mode
# @return : <str>
def gameMode(tab):
	gameModeMessage = """Welcome to the 'Puissance 4' game !
Please choose a mode"""
	gameModeMessage = concatLoopArray(tab, gameModeMessage)
	gameModeMessage += "\nGame mode :\n"
	return input(gameModeMessage)

# @description : This function gives the possibility to the user to choose a bot difficulty
# @return : <str>
def botLevel(tab):
	botLevelMessage = "\n1vsCPU - Choose the difficulty for your oponent :"
	botLevelMessage = concatLoopArray(tab, botLevelMessage)
	botLevelMessage += "\nLevel :\n"
	return input(botLevelMessage)

# @description : This function gives the possibility to the user to choose a bot profile
# @return : <str>
def botProfile(tab):
	botProfileMessage = "\n1vsCPU - Choose the profile for your oponent :"
	botProfileMessage = concatLoopArray(tab, botProfileMessage)
	botProfileMessage += "\nProfile :\n"
	return input(botProfileMessage)

# @description : This function is the main function of the game
# it start the process and asks to the user all the questions needed
# @return : <array> tabGame
def start():
	# Declare predifined arrays with all the options given in prompted message
	tabMode = ["1vs1", "2vs2", "CPUvsCPU", "1vsCPU"]
	tabBotLevel = ["Easy", "Normal", "Hard", "Extreme", "Hell"]
	tabBotProfile = ["Aggressive", "Passive", "Equilibrate", "Stupid"]
	tabGame = []

	gameModeInt = int(gameMode(tabMode))
	mode = tabMode[gameModeInt-1]
	tabGame.append(mode)

	# If game mode is 1vsCPU, we launch the level and profile options
	if(mode == "1vsCPU"):
		botLevelInt = int(botLevel(tabBotLevel))
		botProfileInt = int(botProfile(tabBotProfile))
		tabGame.append(tabBotLevel[botLevelInt-1])
		tabGame.append(tabBotProfile[botProfileInt-1])

	return tabGame

print start()
