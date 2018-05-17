from constants import GRID, UI
from grid import Cell

class Shape:
	def __init__(self, game):
		self.game      = game
		self.is_mobile = True
		self.timer     = 0

	def move(self, dr, dc):
		if self.can_move(dr, dc):
			self.cells[0].move(dr, dc)
			self.cells[1].move(dr, dc)
			self.cells[2].move(dr, dc)
			self.cells[3].move(dr, dc)
		else:
			if dr == 1:
				self.freeze()

	def can_move(self, dr, dc):
		return self.is_mobile and \
		       self.cells[0].can_move(dr, dc) and \
		       self.cells[1].can_move(dr, dc) and \
		       self.cells[2].can_move(dr, dc) and \
		       self.cells[3].can_move(dr, dc)

	def rotation(self, rot):
		if self.can_rotate(rot):
			self.cells[0].move(rot[0][0], rot[0][1])
			self.cells[1].move(rot[1][0], rot[1][1])
			self.cells[2].move(rot[2][0], rot[2][1])
			self.cells[3].move(rot[3][0], rot[3][1])

			self.position = (self.position + 1) % 4

	def can_rotate(self, rot):
		return self.is_mobile and \
		       self.cells[0].can_move(rot[0][0], rot[0][1]) and \
		       self.cells[1].can_move(rot[1][0], rot[1][1]) and \
		       self.cells[2].can_move(rot[2][0], rot[2][1]) and \
		       self.cells[3].can_move(rot[3][0], rot[3][1])

	def freeze(self):
		self.is_mobile  = False
		self.game.shape = None

		for cell in self.cells:
			self.game.grid.get_cell(cell.row, cell.col).color = cell.color

	def is_overlapping(self):
		return self.game.grid.cell_occupied(self.cells[0].row, self.cells[0].col) or \
		       self.game.grid.cell_occupied(self.cells[1].row, self.cells[1].col) or \
		       self.game.grid.cell_occupied(self.cells[2].row, self.cells[2].col) or \
		       self.game.grid.cell_occupied(self.cells[3].row, self.cells[3].col)

	def update(self, dt):
		if self.is_mobile:
			self.timer += dt

			if self.timer >= GRID['drop_timer']:
				self.timer = 0
				self.move(1, 0)

	def draw(self, screen):
		for cell in self.cells:
			cell.draw(screen)

class BlueShape(Shape):
	def __init__(self, game, row, col):
		self.position = 0
		self.cells    = [
			Cell(game.grid, row - 1, col + 0, UI['color']['blue']),
			Cell(game.grid, row + 0, col + 0, UI['color']['blue']),
			Cell(game.grid, row + 1, col + 0, UI['color']['blue']),
			Cell(game.grid, row + 1, col - 1, UI['color']['blue'])
		]

		Shape.__init__(self, game)

	def rotate(self):
		if self.position == 0:
			rot = [ [1, 1], [0, 0], [-1, -1], [-2, 0] ]
		elif self.position == 1:
			rot = [ [1, -1], [0, 0], [-1, 1], [0, 2] ]
		elif self.position == 2:
			rot = [ [-1, -1], [0, 0], [1, 1], [2, 0] ]
		else:
			rot = [ [-1, 1], [0, 0], [1, -1], [0, -2] ]

		self.rotation(rot)

class RedShape(Shape):
	def __init__(self, game, row, col):
		self.position = 0
		self.cells    = [
			Cell(game.grid, row - 1, col + 0, UI['color']['red']),
			Cell(game.grid, row + 0, col + 0, UI['color']['red']),
			Cell(game.grid, row + 1, col + 0, UI['color']['red']),
			Cell(game.grid, row + 1, col + 1, UI['color']['red'])
		]

		Shape.__init__(self, game)

	def rotate(self):
		if self.position == 0:
			rot = [ [1, 1], [0, 0], [-1, -1], [0, -2] ]
		elif self.position == 1:
			rot = [ [1, -1], [0, 0], [-1, 1], [-2, 0] ]
		elif self.position == 2:
			rot = [ [-1, -1], [0, 0], [1, 1], [0, 2] ]
		else:
			rot = [ [-1, 1], [0, 0], [1, -1], [2, ] ]

		self.rotation(rot)

class GreenShape(Shape):
	def __init__(self, game, row, col):
		self.position = 0
		self.cells    = [
			Cell(game.grid, row - 1, col + 1, UI['color']['green']),
			Cell(game.grid, row - 1, col + 0, UI['color']['green']),
			Cell(game.grid, row + 0, col + 0, UI['color']['green']),
			Cell(game.grid, row + 0, col - 1, UI['color']['green'])
		]

		Shape.__init__(self, game)

	def rotate(self):
		if self.position == 0:
			rot = [ [1, -1], [0, 0], [-1, -1], [-2, 0] ]
		elif self.position == 1:
			rot = [ [-1, -1], [0, 0], [-1, 1], [0, 2] ]
		elif self.position == 2:
			rot = [ [-1, 1], [0, 0], [1, 1], [2, 0] ]
		else:
			rot = [ [1, 1], [0, 0], [1, -1], [0, -2] ]

		self.rotation(rot)

class PurpleShape(Shape):
	def __init__(self, game, row, col):
		self.position = 0
		self.cells    = [
			Cell(game.grid, row - 1, col - 1, UI['color']['purple']),
			Cell(game.grid, row - 1, col + 0, UI['color']['purple']),
			Cell(game.grid, row + 0, col + 0, UI['color']['purple']),
			Cell(game.grid, row + 0, col + 1, UI['color']['purple'])
		]

		Shape.__init__(self, game)

	def rotate(self):
		if self.position == 0:
			rot = [ [-1, 1], [0, 0], [-1, -1], [0, -2] ]
		elif self.position == 1:
			rot = [ [1, 1], [0, 0], [-1, 1], [-2, 0] ]
		elif self.position == 2:
			rot = [ [1, -1], [0, 0], [1, 1], [0, 2] ]
		else:
			rot = [ [-1, -1], [0, 0], [1, -1], [2, 0] ]

		self.rotation(rot)

class OrangeShape(Shape):
	def __init__(self, game, row, col):
		self.position = 0
		self.cells    = [
			Cell(game.grid, row - 1, col + 0, UI['color']['orange']),
			Cell(game.grid, row - 1, col + 1, UI['color']['orange']),
			Cell(game.grid, row + 0, col + 0, UI['color']['orange']),
			Cell(game.grid, row + 0, col + 1, UI['color']['orange'])
		]

		Shape.__init__(self, game)

	def rotate(self):
		if self.position == 0:
			rot = [ [0, 0], [0, 0], [0, 0], [0, 0] ]
		elif self.position == 1:
			rot = [ [0, 0], [0, 0], [0, 0], [0, 0] ]
		elif self.position == 2:
			rot = [ [0, 0], [0, 0], [0, 0], [0, 0] ]
		else:
			rot = [ [0, 0], [0, 0], [0, 0], [0, 0] ]

		self.rotation(rot)

class GreyShape(Shape):
	def __init__(self, game, row, col):
		self.position = 0
		self.cells    = [
			Cell(game.grid, row - 1, col + 0, UI['color']['grey']),
			Cell(game.grid, row + 0, col + 0, UI['color']['grey']),
			Cell(game.grid, row + 0, col - 1, UI['color']['grey']),
			Cell(game.grid, row + 0, col + 1, UI['color']['grey'])
		]

		Shape.__init__(self, game)

	def rotate(self):
		if self.position == 0:
			rot = [ [1, 1], [0, 0], [-1, 1], [1, -1] ]
		elif self.position == 1:
			rot = [ [1, -1], [0, 0], [1, 1], [-1, -1] ]
		elif self.position == 2:
			rot = [ [-1, -1], [0, 0], [1, -1], [-1, 1] ]
		else:
			rot = [ [-1, 1], [0, 0], [-1, -1], [1, 1] ]

		self.rotation(rot)

class YellowShape(Shape):
	def __init__(self, game, row, col):
		self.position = 0
		self.cells    = [
			Cell(game.grid, row - 1, col + 0, UI['color']['yellow']),
			Cell(game.grid, row + 0, col + 0, UI['color']['yellow']),
			Cell(game.grid, row + 1, col + 0, UI['color']['yellow']),
			Cell(game.grid, row + 2, col + 0, UI['color']['yellow'])
		]

		Shape.__init__(self, game)

	def rotate(self):
		if self.position == 0:
			rot = [ [1, 1], [0, 0], [-1, -1], [-2, -2] ]
		elif self.position == 1:
			rot = [ [1, -1], [0, 0], [-1, 1], [-2, 2] ]
		elif self.position == 2:
			rot = [ [-1, -1], [0, 0], [1, 1], [2, 2] ]
		else:
			rot = [ [-1, 1], [0, 0], [1, -1], [2, -2] ]

		self.rotation(rot)
