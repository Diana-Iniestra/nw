import random
import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NAVY = (0, 0, 128)
DEEP_SKY_BLUE = (0, 191, 255)
DARK_TURQUOISE = (0, 206, 209)
STEEL_BLUE = (70, 130, 180)
BLUE = (0, 0, 255)
MEDIUM_BLUE = (0, 0, 205)
CORNFLOWER_BLUE = (100, 149, 237)
DODGER_BLUE = (30, 144, 255)
colors = [BLACK, NAVY, DEEP_SKY_BLUE, DARK_TURQUOISE, 
         STEEL_BLUE, BLUE, MEDIUM_BLUE, CORNFLOWER_BLUE, DODGER_BLUE]

SCREEN_SIZE = screen_width, screen_height = 1000, 700
width = random.randrange(5, 10, 1)

number_of_circles = 35

class Circle:
	def __init__(self, x, y, radius, color, width):
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

screen = pygame.display.set_mode(SCREEN_SIZE) 

xy_cor = [[150,400],[150,600],[350,400],[350,600],
          [200,450],[200,550],[300,450],[300,550],
          [175,425],[175,575],[225,475],[225,525],
          [275,475],[275,525],[325,425],[325,575],
          [250,500],
          [650,400],[650,420],[650,450],[650,480],
          [650,500],[650,520],[650,550],[650,580],
          [650,600],
          [900,400],[750,600],[750,400],[750,480],
          [750,400],[780,400],[840,400],[880,400],
          [800,400]]
circles = []

for cor in range(number_of_circles):
	radius = random.randint(20, 25)
	x = xy_cor[cor][0]
	y = xy_cor[cor][1]
	color = random.choice(colors)
	circles.append(Circle(x, y, radius, color, width))

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