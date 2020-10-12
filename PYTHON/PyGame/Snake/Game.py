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
    Borders.append(Tile.Tile(10,10,i,5,(0,0,0)))
    Borders.append(Tile.Tile(10,10,i,WIDTH-5,(0,0,0)))
    i+=10
i=0
while i<= WIDTH:
    Borders.append(Tile.Tile(10,10,5,i,(0,0,0)))
    Borders.append(Tile.Tile(10,10,WIDTH-5,i,(0,0,0)))
    i+=10
for i in Borders:
    AllSprite.add(i)
    i.Direction=""
Food = Tile.Food(10,10,WIDTH,HEIGHT,Player)
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
            if event.key == pygame.K_RIGHT:
                Player[0].ChangeDirection("R")
            if event.key == pygame.K_UP:
                Player[0].ChangeDirection("U")
            if event.key == pygame.K_DOWN:
                Player[0].ChangeDirection("D")
    if Player[0].Check(Borders):
        break
    if Player[0].Check(Player[1:len(Player)]):
        break
    if Player[0].rect.center == Food.rect.center:
        AllSprite.remove(Food)
        Food = Tile.Food(10,10,WIDTH,HEIGHT,Player)
        Player.append(Tile.Tile(10,10,Player[-1].rect.y,Player[-1].rect.x,(0,255,0)))
        Player[-1].Direction="F"
        AllSprite.add(Player[-1])
        AllSprite.add(Food)
    pygame.display.flip()
    AllSprite.update()
    for i in range(1,len(Player)):
        Player[i].rect.x = Player[i-1].NextPosition[0]
        Player[i].rect.y = Player[i-1].NextPosition[1]
    screen.fill((255,255,255))
    AllSprite.draw(screen)
    clock.tick(FPS)
pygame.quit()