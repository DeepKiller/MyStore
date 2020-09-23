import pygame
import random
WIDTH = 1000
HEIGHT = 1000
FPS = 60
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((255,0,0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(FPS)
pygame.quit()