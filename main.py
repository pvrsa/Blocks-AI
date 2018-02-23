from block import Block
import random
import pygame


colour = {}
colour["W"] = (255,255,255)
colour["B"] = (0,0,0)
colour["R"] = (255,0,0)
colour["G"] = (0,255,0)
colour["B"] = (0,0,255)

SCREENWIDTH=600
SCREENHEIGHT=600

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BLocks AI")

all_sprites_list = pygame.sprite.Group()

A = Block(colour["R"] , 100, 100 , 'A')
A.rect.x = 0
A.rect.y = 300

Ground = Block(colour["G"] , 600, 200)
Ground.rect.x = 0
Ground.rect.y = 400

all_sprites_list.add(A)
all_sprites_list.add(Ground)


gameExit = False
rectangle_draging = False

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
			
		elif pygame.mouse.get_pressed()[0]:
			mousex,mousey = event.pos
			if A.rect.collidepoint(mousex,mousey):
				A.rect.x=mousex-A.rect.width/2
				A.rect.y=mousey-A.rect.height/2

	screen.fill(colour["W"])
	all_sprites_list.draw(screen)
	pygame.display.flip()

pygame.quit()	