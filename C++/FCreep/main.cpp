#include "World.cpp"
#include "Graphic.cpp"

int main()
{
    World world = World((TileOnScreen + TileSize) * 2, time(0));
    Draw(&world);
}