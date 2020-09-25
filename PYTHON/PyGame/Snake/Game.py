import pygame
import random
import Tile

WIDTH = 500
HEIGHT = 500
FPS = 2


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
running = True
screen.fill((255,255,255))
AllSprite = pygame.sprite.Group()
Player = list()
Player.append(Tile.Tile(10,10,WIDTH/2,HEIGHT/2,(0,255,0)))
Borders = list()
#Borders.append(Player)
i=0
while i <= HEIGHT:
    Borders.append(Tile.Tile(10,10,i,0,(0,0,0)))
    Borders.append(Tile.Tile(10,10,i,WIDTH,(0,0,0)))
    i+=10
i=0
while i<= WIDTH:
    Borders.append(Tile.Tile(10,10,0,i,(0,0,0)))
    Borders.append(Tile.Tile(10,10,WIDTH,i,(0,0,0)))
    i+=10
for i in Borders:
    AllSprite.add(i)
    i.Direction=""
Food = Tile.Food(10,10,WIDTH,HEIGHT)
CORX,CORY = (0,10)
AllSprite.add(Food)
AllSprite.add(Player[0])
while running:
    print("Player:"+str(Player[0].rect.center)+" Food:" + str(Food.rect.center)+" Player size:" + str(len(Player)))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player[0].ChangeDirection("L")
                CORY,CORX=(0,10)
            if event.key == pygame.K_RIGHT:
                Player[0].ChangeDirection("R")
                CORY,CORX=(0,-10)
            if event.key == pygame.K_UP:
                Player[0].ChangeDirection("U")
                CORX,CORY=(0,10)
            if event.key == pygame.K_DOWN:
                Player[0].ChangeDirection("D")
                CORX,CORY=(0,-10)
    if Player[0].CheckLose(Borders):
        break
    if Player[0].rect.center == Food.rect.center:
        AllSprite.remove(Food)
        Food = Tile.Food(10,10,WIDTH,HEIGHT)
        Player.append(Tile.Tile(10,10,Player[-1].rect.y,Player[-1].rect.x,(0,255,0)))
        Player[-1].Direction="F"
        AllSprite.add(Player[-1])
        AllSprite.add(Food)
    for i in range(1,len(Player)):
        if Player[i].NextDirection == "U":
        Player[i].rect.x = Player[i-1].rect.x+CORX
        Player[i].rect.y = Player[i-1].rect.y+CORY
        if i > 2 and Player[0].rect.center == Player[i].rect.center:
            break
    pygame.display.flip()
    AllSprite.update()
    screen.fill((255,255,255))
    AllSprite.draw(screen)
    clock.tick(FPS)
pygame.quit()