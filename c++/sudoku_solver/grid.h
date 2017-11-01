#ifndef GRID_H
#define GRID_H

#include <vector>

using namespace std;

class grid
{
private:
    int finalValue;
    vector<int> possibilities;

public:
    grid() : possibilities(1,2,3,4,5,6,7,8,9)
    {}

    void removeFromPossibilities(int value);
};

#endif // GRID_H
