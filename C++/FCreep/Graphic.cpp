#include <SFML/Graphics.hpp>
#include "iostream"
#include "World.cpp"

using namespace sf;

ContextSettings settings(0, 0, 4, 1, 1, 0, false);

const int TileSize = 10 * 3;
const int TileOnScreen = 30;

RenderWindow Wind(VideoMode(TileSize *TileOnScreen, TileSize *TileOnScreen), "FCreeps", Style::Default, settings);

struct Point
{
    int x = TileSize;
    int y = TileSize;
};

void DrawLines(RenderWindow *wnd, Vector2f point1, Vector2f point2)
{
    Vertex line[] = {
        Vertex(point1),
        Vertex(point2)};
    wnd->draw(line, 2, Lines);
}

bool **Slice(const World *w, int min, int max)
{
    bool **out = new bool *[w->Size];
    for (int i = 0; i < w->Size; i++)
    {
        out[i] = new bool[w->Size];
        for (int j = 0; j < w->Size; j++)
        {
            if (w->WorldArray[i][j] > min && w->WorldArray[i][j] <= max)
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

void GenerateShape(World *w, RenderWindow *wnd, int x, int y, int posx, int posy)
{
    if (x - 1 < 0 || y - 1 < 0 || x + 1 > w->Size || y + 1 > w->Size)
    {
        return;
    }

    int stp = TileSize / 3;
    int coordx = y * TileSize - posy;
    int coordy = x * TileSize - posx;
    Text text;
    Font font;
    font.loadFromFile("arial.ttf");
    text.setFont(font);
    text.setCharacterSize(stp);
    text.setString(std::to_string(w->WorldArray[x][y]));
    text.setPosition(Vector2f(coordx + stp, coordy + stp));
    wnd->draw(text);

    int linesCount = 0;
    int rectCount = 0;

    for (int xi = x - 1; xi <= x + 1; xi++)
    {
        for (int yi = y - 1; yi <= y + 1; yi++)
        {
            if (w->WorldArray[xi][yi] != w->WorldArray[x][y])
            {
                linesCount++;
                if ((xi == x - 1 && yi == y) || (xi == x && yi == y - 1) || (xi == x && yi == y + 1) || (xi == x + 1 && yi == y))
                {
                    rectCount++;
                }
            }
        }
    }

    if (linesCount < 2 || rectCount == 0)
    {
        return;
    }

    for (int xi = x - 1; xi <= x + 1; xi++)
    {
        for (int yi = y - 1; yi <= y + 1; yi++)
        {
            if (w->WorldArray[xi][yi] != w->WorldArray[x][y])
            {
                // (0 1,1 0) (1 0,2 0) (2 0,3 1)
                // (0 1,0 2) (000,000) (3 2,3 1)
                // (0 2,1 3) (1 3,2 3) (2 3,3 2)
                if (xi == x - 1 && yi == y - 1)
                {
                    DrawLines(wnd, Vector2f(coordx, 1 * stp + coordy), Vector2f(1 * stp + coordx, coordy));
                }
                else if (xi == x - 1 && yi == y)
                {
                    DrawLines(wnd, Vector2f(1 * stp + coordx, coordy), Vector2f(2 * stp + coordx, coordy));
                }
                else if (xi == x - 1 && yi == y + 1)
                {
                    DrawLines(wnd, Vector2f(2 * stp + coordx, coordy), Vector2f(3 * stp + coordx, 1 * stp + coordy));
                }
                else if (xi == x && yi == y - 1)
                {
                    DrawLines(wnd, Vector2f(coordx, 1 * stp + coordy), Vector2f(coordx, 2 * stp + coordy));
                }
                else if (xi == x && yi == y + 1)
                {
                    DrawLines(wnd, Vector2f(3 * stp + coordx, 2 * stp + coordy), Vector2f(3 * stp + coordx, 1 * stp + coordy));
                }
                else if (xi == x + 1 && yi == y - 1)
                {
                    DrawLines(wnd, Vector2f(coordx, 2 * stp + coordy), Vector2f(1 * stp + coordx, 3 * stp + coordy));
                }
                else if (xi == x + 1 && yi == y)
                {
                    DrawLines(wnd, Vector2f(1 * stp + coordx, 3 * stp + coordy), Vector2f(2 * stp + coordx, 3 * stp + coordy));
                }
                else if (xi == x + 1 && yi == y + 1)
                {
                    DrawLines(wnd, Vector2f(2 * stp + coordx, 3 * stp + coordy), Vector2f(3 * stp + coordx, 2 * stp + coordy));
                }
            }
        }
    }
}

void Draw(World *world)
{
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
            else if (event.type == Event::KeyPressed) //Keyboard Events
            {
                if (Keyboard::isKeyPressed(Keyboard::Up))
                {
                    point.x -= point.x - TileSize > 0 ? TileSize : 0;
                }
                else if (Keyboard::isKeyPressed(Keyboard::Down))
                {
                    point.x += point.x + TileSize < (world->Size - TileOnScreen) * TileSize ? TileSize : 0;
                }
                else if (Keyboard::isKeyPressed(Keyboard::Left))
                {
                    point.y -= point.y - TileSize > 0 ? TileSize : 0;
                }
                else if (Keyboard::isKeyPressed(Keyboard::Right))
                {
                    point.y += point.y + TileSize < (world->Size - TileOnScreen) * TileSize ? TileSize : 0;
                }
                else if (Keyboard::isKeyPressed(Keyboard::Space))
                {
                    world->Smooth();
                }
                else if (Keyboard::isKeyPressed(Keyboard::Escape))
                {
                    Wind.close();
                }
                changed = true;
            }
        }

        if (changed)
        {
            Wind.clear();
            for (int x = point.x; x < (TileSize * TileOnScreen) + point.x; x += TileSize)
            {
                for (int y = point.y; y < (TileSize * TileOnScreen) + point.y; y += TileSize)
                {
                    GenerateShape(world, &Wind, x / TileSize, y / TileSize, point.x, point.y);
                }
            }
            changed = false;
            Wind.display();
        }
    }
}