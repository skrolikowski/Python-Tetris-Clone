import pygame
from constants import UI, GRID

# Grid object
class Grid:
	def __init__(self, game, rows, cols):
		self.game  = game
		self.rows  = rows
		self.cols  = cols
		self.cells = []

		for r in range(rows):
			for c in range(cols):
				self.cells.append(Cell(self, r, c))

	def cell_occupied(self, row, col):
		return self.get_cell(row, col).is_occupied()

	def is_cell(self, row, col):
		return row >= 0 and row < self.rows and col >= 0 and col < self.cols

	def get_cell(self, row, col):
		return self.cells[col + row * self.cols]

	def clear_complete_rows(self):
		for r in range(self.rows, 0, -1):
			cells_occupied = 0

			for c in range(self.cols):
				if self.is_cell(r, c) and self.cell_occupied(r, c):
					cells_occupied += 1

			if cells_occupied == self.cols:
				self.clear_row(r)

	def clear_row(self, row):
		for r in range(row, 0, -1):
			for c in range(self.cols):
				self.get_cell(r, c).color = self.get_cell(r - 1, c).color

		for c in range(self.cols):
			self.get_cell(0, c).color = None

	def draw(self, screen):
		for cell in self.cells:
			cell.draw(screen)

# Cell object
class Cell:
	def __init__(self, grid, row, col, color = None):
		self.grid   = grid
		self.row    = row
		self.col    = col
		self.color  = color

	def container(self):
		x = self.col * GRID['cell']
		y = self.row * GRID['cell']
		w = GRID['cell']
		h = GRID['cell']

		return [x, y, w, h]

	def is_occupied(self):
		return self.color != None

	def can_move(self, dr, dc):
		nextRow = self.row + dr
		nextCol = self.col + dc

		return self.grid.is_cell(nextRow, nextCol) and \
		       not self.grid.cell_occupied(nextRow, nextCol)

	def move(self, dr, dc):
		self.row += dr
		self.col += dc

	def draw(self, screen):
		if self.color == None:
			pygame.draw.rect(screen, UI['color']['border'], self.container(), 1)
		else:
			pygame.draw.rect(screen, self.color, self.container(), 0)
