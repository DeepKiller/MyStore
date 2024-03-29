#include <SFML/Graphics.hpp>
#include "iostream"
#include "World.cpp"
#include "math.h"

using namespace sf;

ContextSettings settings(0, 0, 4, 1, 1, 0, false);

int TileSize = 10;
int TileOnScreen = 100;
const int CountSlice = 30;

RenderWindow Wind(VideoMode(TileSize *TileOnScreen, TileSize *TileOnScreen), "FCreeps", Style::Default, settings);

struct Point
{
    int x = TileSize;
    int y = TileSize;
};

bool **Slice(const World *w, int min, int max)
{
    bool **out = new bool *[w->Size];
    for (int i = 0; i < w->Size; i++)
    {
        out[i] = new bool[w->Size];
        for (int j = 0; j < w->Size; j++)
        {
            if (w->WorldArray[i][j] >= min && w->WorldArray[i][j] <= max)
            {
                out[i][j] = true;
            }
            else
            {
                out[i][j] = false;
            }
        }
    }

    return out;
}

void GenerateShape(World *w, RenderWindow *wnd, int posx, int posy, bool **layer, int index)
{
    for (int xi = posx; xi < posx + (TileSize * TileOnScreen); xi += TileSize)
    {
        for (int yi = posy; yi < posy + (TileSize * TileOnScreen); yi += TileSize)
        {
            if (layer[xi / TileSize][yi / TileSize])
            {
                int coordx = xi - posx;
                int coordy = yi - posy;
                RectangleShape rect(Vector2f(TileSize, TileSize));
                rect.setPosition(Vector2f(coordx, coordy));
                int blue = index * 255 / CountSlice * 2;
                int green = blue < 255 ? 0 : (CountSlice - index) * 255 / CountSlice * 2;
                rect.setFillColor(Color(0, green, blue, 255));
                wnd->draw(rect);
            }
        }
    }
}

void Draw(World *world)
{
    bool ***sliceses = new bool **[CountSlice];
    Point point;
    bool changed = true;
    while (Wind.isOpen())
    {
        Event event;

        while (Wind.pollEvent(event))
        {
            //Window Events
            if (event.type == Event::Closed)
            {
                Wind.close();
            }
            else if (event.type == Event::KeyPressed || event.type == Event::MouseButtonPressed) //Keyboard Events
            {
                if (Keyboard::isKeyPressed(Keyboard::Left))
                {
                    point.x -= point.x - TileSize > 0 ? TileSize : 0;
                }
                if (Keyboard::isKeyPressed(Keyboard::Right))
                {
                    point.x += point.x + TileSize < (world->Size - TileOnScreen) * TileSize ? TileSize : 0;
                }
                if (Keyboard::isKeyPressed(Keyboard::Up))
                {
                    point.y -= point.y - TileSize > 0 ? TileSize : 0;
                }
                if (Keyboard::isKeyPressed(Keyboard::Down))
                {
                    point.y += point.y + TileSize < (world->Size - TileOnScreen) * TileSize ? TileSize : 0;
                }
                if (Keyboard::isKeyPressed(Keyboard::Space))
                {
                    world->Smooth();
                }
                if (Keyboard::isKeyPressed(Keyboard::Escape))
                {
                    Wind.close();
                }
                if (Keyboard::isKeyPressed(Keyboard::Add))
                {
                    if (TileSize < 100)
                    {
                        TileSize += TileSize;
                    }
                }
                else if (Keyboard::isKeyPressed(Keyboard::Subtract))
                {
                    if (TileSize > 1)
                    {
                        TileSize -= TileSize;
                    }
                }
                if (Mouse::isButtonPressed(Mouse::Left))
                {

                    int coordx = Mouse::getPosition().x - Wind.getPosition().x;
                    int coordy = Mouse::getPosition().y - Wind.getPosition().y;
                    cout << coordx << " " << coordy << endl;

                    int xi = coordx / TileSize + 1 + point.x;
                    int yi = coordy / TileSize + 1 + point.y;

                    cout << world->WorldArray[xi][yi] << endl;
                }
                TileOnScreen = min(Wind.getSize().x / TileSize, Wind.getSize().y / TileSize);
                changed = true;
            }
        }
        if (changed)
        {
            Wind.clear();

            for (int i = 0, size = world->MaxValue * 2 + 1; i < CountSlice; i++)
            {
                sliceses[i] = Slice(world, i * (size / CountSlice) - world->MaxValue, (i + 1) * (size / CountSlice) - world->MaxValue);
            }
            for (int i = 0; i < CountSlice; i++)
            {
                GenerateShape(world, &Wind, point.x, point.y, sliceses[i], i);
            }

            changed = false;
            Wind.display();
        }
    }
}