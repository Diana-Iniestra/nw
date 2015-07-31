import random
import math
from euclid import Vector2
from pygame.locals import QUIT
import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 700, 500
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
FPS_LIMIT = 60 # Frames Per Second
DRAG = 1
width = random.randrange(0, 10, 1)

class Circle:
	def __init__(self, position, velocity, accel, radius, color, width):
		self.position = position
		self.velocity = velocity
		self.accel = accel
		self.radius = radius
		self.color = color
		self.width = width

	def _bounce(self):
		left_margin = self.radius
		right_margin = SCREEN_WIDTH - self.radius
		top_margin = self.radius
		bottom_margin = SCREEN_HEIGHT - self.radius

		# Check for collision with left or right wall
		# Push the circle inwards and reflect the velocity through the y-axis
		if self.position.x <= left_margin:
			self.position.x = 2*left_margin - self.position.x
			self.velocity = self.velocity.reflect(Vector2(1, 0))
		elif self.position.x >= right_margin:
			self.position.x = 2*right_margin - self.position.x
			self.velocity = self.velocity.reflect(Vector2(1, 0))

		# Check for collision with top or bottom wall
		# Push the circle inwards and reflect the velocity through the x-axis
		if self.position.y <= top_margin:
			self.position.y = 2*top_margin - self.position.y
			self.velocity = self.velocity.reflect(Vector2(0, 1))
		elif self.position.y >= bottom_margin:
			self.position.y = 2*bottom_margin - self.position.y
			self.velocity = self.velocity.reflect(Vector2(0, 1))

	def _get_next_positon(self, dt):
		return self.position + 0.5 * self.accel * dt**2 + self.velocity * dt

	def draw(self, surface):
		pos = (int(self.position.x), int(self.position.y))
		pygame.draw.circle(
			surface,
			self.color,
			pos,
			self.radius,
			self.width
			)

	def collide(self, other):
		collision_vector = (self.position - other.position).normalize()
		self.velocity = self.velocity.reflect(collision_vector)
		other.velocity = other.velocity.reflect(collision_vector)

	def surface_distance(self, other, dt):
		# Equation for distsnce between surfaces
		# d(t) = ||pos1(t) - pos2(t)|| - (r1 + r2)
		pos1 = self._get_next_positon(dt)
		pos2 = other._get_next_positon(dt)
		return abs(pos1 - pos2) - (self.radius + other.radius)

	def move(self, dt):
		self.velocity = self.velocity + self.accel*dt - DRAG*self.velocity*dt
		self.position = self._get_next_positon(dt)
		self._bounce()

def get_random_velocity(speed):
	angle = random.uniform(0, 2*math.pi)
	x = math.cos(angle)
	y = math.sin(angle)
	unit_vector = Vector2(x, y)
	return speed * unit_vector

def main():
	colors = [NAVY, DARK_TURQUOISE, STEEL_BLUE, BLUE, MEDIUM_BLUE, 
			  CORNFLOWER_BLUE, DODGER_BLUE]
	color_screen = [WHITE, BLACK]
	speed = 100 # Pixels per second
	number_of_circles = 35
	gravity = Vector2(0, -10) # Pixels per second per second

	# Initialize the display window
	screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

	# Create a lsit of circles with random positions, radii and velocities
	circles = []
	for i in range(number_of_circles):
		radius = random.randint(10, 30)
		x = random.randint(radius, SCREEN_WIDTH - radius)
		y = random.randint(radius, SCREEN_HEIGHT - radius)
		position = Vector2(x, y)
		velocity = get_random_velocity(speed)
		color = random.choice(colors)
		circles.append(Circle(position, velocity, gravity, radius, color, width))

	# Game Looop 
	clock = pygame.time.Clock()
	running = True

	while running:
		# Break out of game loop if the window is closed
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False

		# Get the time elapsed
		dt_ms = clock.tick(FPS_LIMIT)
		dt = dt_ms / 1000.0

		for colour in color_screen:
			screen.fill(colour)

		# Move the circles and draw them
		for i, circle in enumerate(circles):
			circle.move(dt)
			for other_circle in circles[i+1:]:
				if circle.surface_distance(other_circle, dt) <= 0:
					circle.collide(other_circle)

		for circle in circles:
			circle.draw(screen)

		# Replace the display window
		pygame.display.flip()

	pygame.quit()

if __name__ == '__main__':
	main()


