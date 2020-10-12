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
        if (self.Direction == "U" and not NewDir == "D") or (self.Direction == "D" and not NewDir == "U") or (self.Direction == "R" and not NewDir == "L") or (self.Direction == "L" and not NewDir == "R"):
            self.Direction = NewDir

    def Check(self,Tiles):
        return pygame.sprite.spritecollide(self, Tiles, False)          

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
    def __init__(self,SizeV,SizeH,WIDTH,HEIGTH,Player):
        self.Size = (SizeV,SizeH)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(self.Size)
        self.image.fill((255,127,127))
        self.rect = self.image.get_rect()
        check = True
        while True:
            i,j = (random.randint(0+50,WIDTH-50),random.randint(0+50,HEIGTH-50))
            for tile in Player:
                if tile.rect.x == i and tile.rect.y ==j:
                    check = False
                    break
                else:
                    check = True
            if check:
                break
        self.rect.center = (i-i%10,j-j%10)
