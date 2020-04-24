class Game:

	def __init__(self, tabMode, tabBotLevel, tabBotProfile):
		self.tabMode = tabMode
		self.tabBotLevel = tabBotLevel
		self.tabBotProfile = tabBotProfile
		self.tabGame = []
		pass

	def getTabMode(self):
		return self.tabMode

	def setTabMode(self, tabMode):
		self.tabMode = tabMode

	def getTabBotLevel(self):
		return self.tabMode

	def setTabBotLevel(self, tabBotLevel):
		self.tabBotLevel = tabBotLevel

	def getTabBotProfile(self):
		return self.tabBotProfile

	def setTabBotProfile(self, tabBotProfile):
		self.tabBotProfile = tabBotProfile

	def getTabGame(self):
		return self.tabGame

	def setTabGame(self, tabGame):
		self.tabGame = tabGame

	def appendToTab(self, tab, value):
		tab.append(value)

	# @description : This function shows the first message of the game and gives the
	# possibility to the user to choose a game mode
	# @return : <str>
	def gameMode(self):
		gameModeMessage = """Welcome to the 'Puissance 4' game !
	Please choose a mode"""
		gameModeMessage = self.concatLoopArray(self.getTabMode(), gameModeMessage)
		gameModeMessage += "\nGame mode :\n"
		return input(gameModeMessage)

	# @description : This function gives the possibility to the user to choose a bot difficulty
	# @return : <str>
	def botLevel(self):
		botLevelMessage = "\n1vsCPU - Choose the difficulty for your oponent :"
		botLevelMessage = self.concatLoopArray(self.getTabBotLevel(), botLevelMessage)
		botLevelMessage += "\nLevel :\n"
		return input(botLevelMessage)

	# @description : This function gives the possibility to the user to choose a bot profile
	# @return : <str>
	def botProfile(self):
		botProfileMessage = "\n1vsCPU - Choose the profile for your oponent :"
		botProfileMessage = self.concatLoopArray(self.getTabBotProfile(), botProfileMessage)
		botProfileMessage += "\nProfile :\n"
		return input(botProfileMessage)

	# @description : This function loop in array and concatenate strings
	# with tab's value by index to format menu -> user friendly
	# @return : <str>
	def concatLoopArray(self, tab, message):
		i = 1
		for mode in tab:
			message += "\n" + str(i) + "- " + tab[i-1]
			i += 1
		return message

	# @description : This function play the actual player moves
	# Update two grids : general grid and personal player grid
	# @return : None
	def moves(self, grid, player, move):
		i = 3
		while len(grid)-i >= 0:
			if grid[len(grid)-i][move-1] == " ":
				grid[len(grid)-i][move-1] = player.getColor()+"O"
				# Update personal grid
				# player['grid'][len(grid)-i][move-1] = "O"
				break
			i += 1

	# @description : This function defines which player can play actual turn
	# @return : <Players>
	def whichTurn(self, players):
		for player in players:
			if(player.getTurn() == True):
				return player

	def endTurn(self, players, player):
		for player in players:
			if(player.getTurn() == True):
				player.setTurn(False)
				player.setMoves(player.getMoves()+1)
			else:
				player.setTurn(True)

	def isGameContinue(self, grid, players):
		# Is Not draw
		for row in grid.getGrid():
		   for value in row:
		    	if(value == " "):
		    		return True
		return False

	def readDiagonal(self, grid):
		HEIGHT = len(grid.getGrid())
		WIDTH = len(grid.getGrid()[0])
		k = 0
		while(k <= HEIGHT+WIDTH-2):
			j = 0
			while(j <= k):
				i = k - j
				if(i < HEIGHT and j < WIDTH):
					if grid.getGrid()[i][j] != " ":
						print grid.getGrid()[i][j]
				j += 1
			k += 1
