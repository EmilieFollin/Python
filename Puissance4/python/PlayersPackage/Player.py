from GamePackage import Grid

class Player:

	def __init__(self, name, color, turn):
		self.name = name
		self.color = color
		self.turn = turn
		self.moves = 0
		self.grid = Grid()

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name

	def getColor(self):
		return self.color

	def setColor(self, color):
		self.color = color

	def getTurn(self):
		return self.turn

	def setTurn(self, turn):
		self.turn = turn

	def getMoves(self):
		return self.moves

	def setMoves(self, moves):
		self.moves = moves

	def getPlayerGrid(self):
		return self.grid

	def setPlayerGrid(self, grid):
		self.grid = grid