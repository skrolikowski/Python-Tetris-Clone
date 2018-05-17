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
		self.grid    = Grid(self, GRID['rows'], GRID['cols'])
		self.sprites = pygame.sprite.Group()
		self.playing = True
		self.shape   = None

	def run(self):
		while self.playing:
			self.dt = clock.tick(WORLD['fps']) / 1000

			self.events()
			self.update()
			self.draw()

		pygame.quit()

	def new_shape(self):
		shape = SHAPE[random.randint(0, len(SHAPE) - 1)]

		return shape(self.grid, 1, 5)

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.quit()
				elif event.key == pygame.K_a:
					self.shape.move(0, -1)
				elif event.key == pygame.K_d:
					self.shape.move(0, 1)
				elif event.key == pygame.K_s:
					self.shape.move(1, 0)
				elif event.key == pygame.K_w:
					self.shape.rotate()

	def quit(self):
		self.playing = False

	def update(self):
		if self.shape == None or not self.shape.is_mobile:
			self.shape = self.new_shape()

		self.shape.update(self.dt)

	def draw(self):
		screen.fill(UI['color']['black'])
		self.grid.draw(screen)
		self.shape.draw(screen)
		pygame.display.flip()

if __name__ == '__main__':
    Game().run()