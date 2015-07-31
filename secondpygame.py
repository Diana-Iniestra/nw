import random
from euclid import Vector2
import pygame
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
colors = [BLACK, RED, GREEN, BLUE]
SCREEN_SIZE = screen_width, screen_height = 600, 400
INITIAL_VELOCITY = 20 #Pixles per second
number_of_circles = 10

class Circle:
	def __init__(self, position, velocity, radius, color, width = 1):
		self.position = position
		self.velocity = velocity
		self.radius = radius
		self.width = width
		self.color = color

	def draw(self, screen_to_draw_on):
		pygame.draw.circle(
			screen_to_draw_on, 
			self.color,
			(int(self.position.x), int(self.position.y)),
			self.radius,
			self.width 
		)

	def move(self, dt):
		self.position = self.position + self.velocity * dt

	# def __repr__(self):
	# 	return "Circle({}, {}, {}, {}, {})".format(
	# 		self.position, self.velocity, self.radius, self.width, self.color)

#Create screen object
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
	radius = random.randint(10, 50)
	x = random.randint(radius, screen_width - radius)
	y = random.randint(radius, screen_height - radius)
	position = Vector2(x,y)
	velocity = Vector2(INITIAL_VELOCITY, 0)	
	color = random.choice(colors)
	circles.append(
		Circle(position, velocity, radius, color)

		)

# --- Game Loop ---

running = True 
clock = pygame.time.Clock()
fps_limit = 60

while running:
	#Gets the time elapsed in milliseconds
	dt_ms = clock.tick(fps_limit) 
	dt = dt_ms / 1000.0 #secnds
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False 

	screen.fill(WHITE)
	for circle in circles:
		circle.move(dt)
		circle.draw(screen)
	#Refresh the screen
	pygame.display.flip() 

pygame.quit()