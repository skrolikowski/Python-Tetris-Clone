import pygame
import random
from constants import *
from grid import Grid

# Game settings
pygame.init()
pygame.display.set_caption("Tetris Clone")
pygame.key.set_repeat(100, 50)

# Global variables
screen = pygame.display.set_mode((WORLD['width'], WORLD['height']))
clock  = pygame.time.Clock()

class Game:
	def __init__(self):
		self.grid      = Grid(self, GRID['rows'], GRID['cols'])
		self.sprites   = pygame.sprite.Group()
		self.playing   = True
		self.game_over = False
		self.shape     = None

	def run(self):
		while self.playing:
			self.dt = clock.tick(WORLD['fps']) / 1000

			self.events()
			self.update()
			self.draw()

		pygame.quit()

	def check_for_game_over(self):
		if self.is_game_over():
			self.game_over = True
			self.quit()

	def is_game_over(self):
		if self.game_over or self.shape == None:
			return True

		return self.shape.is_overlapping()

	def new_shape(self):
		shape = SHAPE[random.randint(0, len(SHAPE) - 1)]

		return shape(self, 1, 5)

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.quit()
				elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
					self.shape.move(0, -1)
				elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					self.shape.move(0, 1)
				elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
					self.shape.move(1, 0)
				elif event.key == pygame.K_w or event.key == pygame.K_UP:
					self.shape.rotate()

	def quit(self):
		self.playing = False

	def update(self):
		if not self.game_over:
			if self.shape == None or not self.shape.is_mobile:
				self.shape = self.new_shape()

			self.check_for_game_over()
			self.shape.update(self.dt)
			self.grid.clear_complete_rows()

	def draw(self):
		screen.fill(UI['color']['black'])
		self.grid.draw(screen)
		
		if self.shape != None:
			self.shape.draw(screen)

		pygame.display.flip()

if __name__ == '__main__':
    Game().run()