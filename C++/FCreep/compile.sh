#!/bin/bash

g++ -c main.cpp
g++ main.o -o FCreep -lsfml-graphics -lsfml-window -lsfml-system
./FCreep