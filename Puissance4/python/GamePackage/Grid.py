class Grid:

	def __init__(self):
		self.grid = [
			[" "," "," "," "," "," "," "], #0
			[" "," "," "," "," "," "," "], #1
			[" "," "," "," "," "," "," "], #2
			[" "," "," "," "," "," "," "], #3
			[" "," "," "," "," "," "," "], #4
			[" "," "," "," "," "," "," "], #5
			["-","-","-","-","-","-","-"], #6
			["1","2","3","4","5","6","7"]  #7
			 #0  #1  #2  #3  #4  #5  #6 <idx^
		]

	def getGrid(self):
		return self.grid

	def setGrid(self, grid):
		self.grid = grid

	# @description : This function shows the actual grid
	# @return : None
	def showGrid(self):
		for row in self.getGrid():
		   for value in row:
		       print '{:4}'.format("\033[1;37;40m"+value),
		   print