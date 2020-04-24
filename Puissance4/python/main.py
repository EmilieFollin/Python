# coding: utf-8

# Packages
# 1- Game -> Game / Grid
# 2- Players -> Players / Human / Bot
# 3- IA -> Level / Profile / (Strategy)

# Class 1 (Game)
# Prompts pour demander à l'utilisateur : mode de jeu, quelle couleur, tu joues quoi, etc.
# Préparer le premier tour / Tester si la partie est finie (gagnée, perdue ou nulle)

# Class 2 (Players)
# Choisir l'emplacement du pion / Attribut couleurs des joueurs
# {
# 	"color" : {
# 		"name" : "red",
# 		"code" : "\033[1;31;40m"
# 	},
# 	"moves" : 0,
# 	"nextPlayer" : True,
# 	"name" : "Florian",
# 	"grid" : [
# 	..
# 	..
# 	..
# 	]
# }

# Class 2-1 (Human)
# ...

# Class 2-2 (Bot)
# Définir un niveau / Définir des stratégies / Jouer son tour / (Prévoir son coup à l'avance)

# Class 3 (Grid)
# Générer une nouvelle partie / Créer la grille / Effacer la grille / Test le placement est autorisé

# Class 4 (Level)

# Class 5 (Profile)

# Class 6 (Strategy)



# MENU de choix de JEU - 1vs1
# Système de tour
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
### Afficher la matrice 2 dimension (X,Y) (génération grille vide)
### Tenter d'ajouter des numéros de lignes/colonnes
### Update de la grille à chaque coup joué + couleur adéquate

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


from GamePackage import *
from PlayersPackage import *

# @description : This function is the main function of the game
# it start the process and asks to the user all the questions needed
# @return : <array> tabGame
def start():
	# Declare predifined arrays with all the options given in prompted message
	tabMode = ["1vs1", "2vs2", "CPUvsCPU", "1vsCPU"]
	tabBotLevel = ["Easy", "Normal", "Hard", "Extreme", "Hell"]
	tabBotProfile = ["Aggressive", "Passive", "Equilibrate", "Stupid"]

	game = Game(tabMode, tabBotLevel, tabBotProfile)
	grid = Grid()

	game.appendToTab(game.getTabGame(), tabMode[game.gameMode()-1])

	# If game mode is 1vsCPU, we launch the level and profile options
	# if(mode == "1vsCPU"):
	# 	botLevelInt = botLevel(tabBotLevel);
	# 	botProfileInt = botProfile(tabBotProfile);
	# 	tabGame.append(tabBotLevel[botLevelInt-1])
	# 	tabGame.append(tabBotProfile[botProfileInt-1])

	# players = {
	# 	"player1" : {
	# 		"color" : {
	# 			"name" : "red",
	# 			"code" : "\033[1;31;40m"
	# 		},
	# 		"moves" : 0,
	# 		"nextPlayer" : True,
	# 		"name" : "Florian"
	# 	},
	# 	"player2" : {
	# 		"color" : {
	# 			"name" : "yellow",
	# 			"code" : "\033[1;33;40m"
	# 		},
	# 		"moves" : 0,
	# 		"nextPlayer" : False,
	# 		"name" : "Jean"
	# 	}
	# }

	# LOOP
	# CHANGE TURN
	# TEST IF GAME END
	#game.readDiagonal(grid)
	j1 = Player("Florian", "\033[1;31;40m", True)
	print j1.getPlayerGrid().showGrid()

	j2 = Player("Paul", "\033[1;33;40m", False)
	players = [j1, j2]
	#checkIfVictory(grid) # false , on continue, true, on arrête	
	while (game.isGameContinue(grid, players)):
		
		# IF player is Human
		### SOIT isinstance(player, Human) True | False
		### SOIT ajouter un attribut "Type" et tester si le Type est Human
		# SI VRAI
		grid.showGrid()
		currentPlayer = game.whichTurn(players)
		print "Turn : " + currentPlayer.getName()
		game.moves(grid.getGrid(), currentPlayer, input("colonne...\n"))
		# SI FAUX
		### C'est le BOT qui joue
		### Analyse du jeu
		###### Analyse de la grille (calcul en %) -> Level <--- 1
		### (Prise de décision -> Profile)
		###### %++ qui gagne. Sauf qu'il faut prendre en considération le 
		###### profil : suivant son profil, le % le plus élevé ne sera pas
		###### forcément le plus intéressant suivant son style de jeu
		###### On décide du coup le plus intéressant
		### Placement du pion <--- 2

		print "_________NEXT TURN_________"
		game.endTurn(players, currentPlayer) # update nextPlayer True -> False (j1)...
		
		
	

	return game.getTabGame()

print start()
