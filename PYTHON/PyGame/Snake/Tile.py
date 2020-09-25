import pygame
import random

class Tile(pygame.sprite.Sprite):
    NextPosition = (0,0)
    Direction = "U" # U = UP D = Down L = Left R = Right
    def __init__(self,SizeV,SizeH,PosY,PosX,Col):
        self.Size = (SizeV,SizeH)
        self.Position = (PosX,PosY)
        self.Color = Col
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(self.Size)
        self.image.fill(self.Color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.Position)
    
    def ChangeDirection(self,NewDir):
        self.Direction = NewDir

    def CheckLose(self,Tiles):
        return pygame.sprite.spritecollide(self, Tiles, False)          

    def CheckFood(self,Food):
        return pygame.sprite.spritecollide(self,Food,False)

    def update(self):
        self.NextPosition = (self.rect.x,self.rect.y)
        if self.Direction == "U":
            self.rect.y-=self.Size[0]
        if self.Direction == "D":
            self.rect.y+=self.Size[0]
        if self.Direction == "R":
            self.rect.x+=self.Size[1]
        if self.Direction == "L":
            self.rect.x-=self.Size[1]
    

class Food(pygame.sprite.Sprite):
    Size =(0,0)
    def __init__(self,SizeV,SizeH,WIDTH,HEIGTH):
        self.Size = (SizeV,SizeH)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(self.Size)
        self.image.fill((255,127,127))
        self.rect = self.image.get_rect()
        i,j = (random.randint(0+50,WIDTH-50),random.randint(0+50,HEIGTH-50))
        self.rect.center = (i-i%10,j-j%10)
