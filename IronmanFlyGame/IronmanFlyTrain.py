import pygame
import time
from random import *

black = (  0,   0,   0)
white = (255, 255, 255)
grey  = (169, 169, 169)
pygame.init()

surfaceWidth  = 800
surfaceHeight = 500

surface = pygame.display.set_mode((surfaceWidth,
								   surfaceHeight)) #window
pygame.display.set_caption('iron man fly train') #title
clock = pygame.time.Clock() #

img = pygame.image.load('ironman_pixel.png') #picture path

imsize = img.get_rect().size
imageWidth  = imsize[0]
imageHeight =  imsize[1]

print(imsize)

def blocks(x_block, y_block, block_width, block_height, gap):
	pygame.draw.rect(surface, white,
					 [x_block, y_block, block_width, block_height],2)
	pygame.draw.rect(surface, white, 
					 [x_block, y_block+block_height+gap, block_width, surfaceHeight-(y_block+block_height+gap)], 2)

def replay_or_quit():
	for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		elif event.type == pygame.KEYDOWN:
			continue

		return event.key
	return None

def makeTextObjs(text, font):
	textSurface = font.render(text, True, grey)
	return textSurface, textSurface.get_rect()

def msgSurface(text):
	smallText = pygame.font.Font('freesansbold.ttf', 20)
	largeText = pygame.font.Font('freesansbold.ttf', 100)

	titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
	titleTextRect.center = surfaceWidth/2, surfaceHeight/2
	surface.blit(titleTextSurf, titleTextRect)

	typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
	typTextRect.center = surfaceWidth/2, (surfaceHeight/2 + 100)
	surface.blit(typTextSurf, typTextRect)

	pygame.display.update()
	time.sleep(1) #time that wait to show the text

	while replay_or_quit() == None:
		clock.tick()

	main()

def gameOver():
	msgSurface('Game Over!')

def ironman(x, y, image): 
	surface.blit(image, (x, y)) #draw img on (x,y)

#########################################################
#game loop
#########################################################
def main():

	num_block = 4
	interWidth = 320
	x_block = [surfaceWidth + interWidth*x for x in range(0,num_block-1)] 
	y_block = 0

	block_width = 75
	gap = imageHeight * 4
	block_height = [randint(0, surfaceHeight-gap) for i in range(0,num_block-1)]
	block_move = 3

	x = 150
	y = 150

	y_move = 0
	x_move = 0

	game_over = False

	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					y_move = -5
				elif event.key == pygame.K_DOWN:
					y_move = 5
				elif event.key == pygame.K_LEFT:
					x_move = -4
				elif event.key == pygame.K_RIGHT:
					x_move = 6

			if event.type == pygame.KEYUP:
				y_move = 0
				x_move = 0

		x, y = pygame.mouse.get_pos()
		#y += y_move
		if y + imageHeight > surfaceHeight:
			y = surfaceHeight - imageHeight
		elif y < 0:
			y = 0

		#x += x_move
		if x + imageWidth > surfaceWidth:
			x = surfaceWidth - imageWidth
		elif x < 0:
			x = 0

		surface.fill(black)
		ironman(x, y, img)

		[blocks(x_block[i], y_block, block_width, block_height[i], gap) for i in range(0, num_block-1)]
		
		for i in range(0, num_block-1):
			x_block[i] -= block_move

		if y > surfaceHeight or y < 0:
			gameOver()

		if x_block[0] < (-block_width):
			x_block.pop(0)
			block_height.pop(0)
			x_block.append(x_block[num_block-3] + interWidth)
			block_height.append(randint(0, surfaceHeight-gap))

		for i in range(0,num_block-1):
			if (x+imageWidth > x_block[i]) and (x+imageWidth < x_block[i] + block_width):
				if (y > (y_block+block_height[i])) and (y+imageHeight < y_block+block_height[i]+gap):
					pass
				else:
					gameOver()
			if (x > x_block[i]) and (x < x_block[i] + block_width):
				if (y > (y_block+block_height[i])) and (y+imageHeight < y_block+block_height[i]+gap):
					pass
				else:
					gameOver()
			
		
		pygame.display.update()
		clock.tick(40)

main()
pygame.quit() #quit game
quit() #quit program