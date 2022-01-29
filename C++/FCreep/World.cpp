#pragma once
#include "random"
#include "iostream"

using namespace std;

class World
{
public:
    int **WorldArray;
    int Size;
    const int MaxValue = 30;

    World(int size, unsigned int seed)
    {
        srand(seed);
        WorldArray = new int *[size];

        for (int x = 0; x < size; x++)
        {
            WorldArray[x] = new int[size];

            for (int y = 0; y < size; y++)
            {
                WorldArray[x][y] = (rand() % (MaxValue * 2 + 1)) - MaxValue;
            }
        }
        Size = size;
    }

    void Smooth()
    {
        for (int x = 1; x < Size - 1; x++)
        {
            for (int y = 1; y < Size - 1; y++)
            {
                int temp[] = {WorldArray[x - 1][y - 1], WorldArray[x - 1][y], WorldArray[x - 1][y + 1],
                              WorldArray[x][y - 1], WorldArray[x][y], WorldArray[x][y + 1],
                              WorldArray[x + 1][y - 1], WorldArray[x + 1][y], WorldArray[x + 1][y + 1]};

                WorldArray[x][y] = Median(temp, 9);
            }
        }
    }

private:
    int Median(int arr[], int size)
    {
        int sum = 0;
        for (int i = 0; i < size; i++)
        {
            sum += arr[i];
        }
        return sum / size + rand() % MaxValue/10;
    }
};