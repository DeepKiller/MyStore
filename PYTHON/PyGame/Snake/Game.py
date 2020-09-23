import pygame
import random
import Tile

WIDTH = 500
HEIGHT = 500
FPS = 5

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
running = True
screen.fill((255,255,255))
AllSprite = pygame.sprite.Group()
Player = Tile.Tile(10,10,WIDTH/2,HEIGHT/2,(0,255,0))
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
AllSprite.add(Food)
AllSprite.add(Player)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player.ChangeDirection("L")
            if event.key == pygame.K_RIGHT:
                Player.ChangeDirection("R")
            if event.key == pygame.K_UP:
                Player.ChangeDirection("U")
            if event.key == pygame.K_DOWN:
                Player.ChangeDirection("D")
    if Player.CheckLose(Borders):
        Player.rect.center=(250,250)
    pygame.display.flip()
    AllSprite.update()
    screen.fill((255,255,255))
    AllSprite.draw(screen)
    clock.tick(FPS)
pygame.quit()