import random
import pygame
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
colors = [BLACK, RED, GREEN, BLUE]

SCREEN_SIZE = screen_width, screen_height = 600, 400

number_of_circles = 10

class Circle:
	def __init__(self, x, y, radius, color, width = 1):
		self.x = x
		self.y = y
		self.radius = radius
		self.width = width
		self.color = color

	def draw(self, screen_to_draw_on):
		pygame.draw.circle(
			screen_to_draw_on, 
			self.color,
			(self.x, self.y),
			self.radius,
			self.width 
		)

	# def __repr__(self):
	# 	return "Circle({}, {}, {}, {}, {})".format(
	# 		self.x, self.y, self.radius, self.width, self.color)

screen = pygame.display.set_mode(SCREEN_SIZE) 

# circles = [
# 	Circle(300, 200, 95),
# 	Circle(100, 100, 20, color = RED),
# 	Circle(10, 20, 5, color = GREEN),
# 	Circle(10, 20, 5, color = BLACK),
# 	Circle(10, 20, 50, color = GREEN),
# 	]

circles = []
for i in range(number_of_circles):
	radius = random.randint(10, 100)
	x = random.randint(radius, screen_width - radius)
	y = random.randint(radius, screen_height - radius)
	color = random.choice(colors)
	circles.append(Circle(x, y, radius, color))

running = True 

while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False 

	#Make the background white
	screen.fill(WHITE)
	#Draw the cirlce on the screen canvas
	for circle in circles:
		circle.draw(screen)
	#Refresh the screen
	pygame.display.flip() 

pygame.quit()
