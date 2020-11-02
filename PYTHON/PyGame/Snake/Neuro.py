import numpy as np
from enum import Enum
import pygame
import Tile

def sigmoid(x):
    # Наша функция активации: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))

GAME = list()

class TILES(Enum):
    SPACE = 0
    WALL = 1
    FOOD = 2
    PLAYER = 3

def Spacer(row,POS):
    size = len(row)
    counter = 0
    for i in range(size-1):
        spaces = int(abs((POS[i+1].rect.x-POS[i].rect.x)//10-size))
        while spaces>0:
            row.insert(counter+1,TILES.SPACE)
            spaces-=1
            counter+=1
        size =0
        counter+=1

def NeuroMind():
    pass

def CallBack(_GAME):
    exit = list()
    for row in _GAME:
        r=list()
        for item in row:
            if type(item) is Tile.Tile:
                if item.IsPlayer:
                    r.append(TILES.PLAYER)
                else:
                    r.append(TILES.WALL)
            if type(item) is Tile.Food:
                r.append(TILES.FOOD)
        if len(r)<50:
            Spacer(r,row)
        exit.append(r)
    GAME=exit
    return NeuroMind()