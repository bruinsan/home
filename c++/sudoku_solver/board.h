#ifndef BOARD_H
#define BOARD_H

#include <vector>
#include "grid.h"

class board
{
private:
    //vector< vector<grid> > g;

public:
    board();
    void checkSudoku();     // check the rows, columns and 3x3 squares


};

#endif // BOARD_H
