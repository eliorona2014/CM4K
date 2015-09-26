import pygame, math, sys
from pygame.locals import *
screen = pygame.display.set_mode((1024,768))
clock = pygame.time.Clock()

class CarSprite(pygame.sprite.Sprite):
	ACELLERATION = 2
	MAX_FORWARD_SPEED = 10
	MAX_REVERSE_SPEED = -5
	TURN_SPEED=5
	
	def __init__(self,image,position):
		pygame.sprite.Sprite.__init__(self)
		self.src_image = pygame.image.load(image)
		self.k_up = self.k_down = self.k_right = self.k_left = 0
		self.speed = self.direction = 0
		self.position = (100,100)

	def update(self,deltat):
		speed +=(k_up+k_down)
		if speed > MAX_FORWARD_SPEED:  speed = MAX_FORWARD_SPEED
		if speed < MAX_REVERSE_SPEED:  speed = MAX_REVERSE_SPEED
		direction +=(k_right+k_left)
		x,y=position
		rad = direction*math.pi/180
		x+=-speed*math.sin(rad)
		y+=-speed*math.cos(rad)
		position=(x,y)
		rotated=pygame.transform.rotate(car,direction)
		rect=rotated.get_rect()
		rect.center=position
		

	



car = pygame.image.load('car.png')

BLACK = (0,0,0)
'''
while True:
	clock.tick(30)
	for event in pygame.event.get():
		if not hasattr(event,'key'): continue
		down = event.type == KEYDOWN
		if event.key ==K_RIGHT : k_right = down * -5
		if event.key ==K_LEFT : k_left = down * 5
		if event.key ==K_UP : k_up = down * 2
		if event.key ==K_DOWN : k_down = down * -2
		if event.key ==K_ESCAPE : sys.exit(0)
	screen.fill(BLACK)
	speed +=(k_up+k_down)
	if speed > MAX_FORWARD_SPEED:  speed = MAX_FORWARD_SPEED
	if speed < MAX_REVERSE_SPEED:  speed = MAX_REVERSE_SPEED
	direction +=(k_right+k_left)
	x,y=position
	rad = direction*math.pi/180
	x+=-speed*math.sin(rad)
	y+=-speed*math.cos(rad)
	position=(x,y)
	rotated=pygame.transform.rotate(car,direction)
	rect=rotated.get_rect()
	rect.center=position
	screen.blit(rotated,rect)
	pygame.display.flip()
'''



