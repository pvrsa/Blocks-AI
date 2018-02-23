import pygame

WHITE = (255, 255, 255)
BLUE = (0,0,255)

class Block(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height,name=""):
        super().__init__()

        pygame.init()
        self.font = pygame.font.SysFont('Arial',35)
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.image.blit(self.font.render(name,True, BLUE ), (40,40))
        pygame.display.update() 
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels