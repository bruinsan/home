#include <iostream>
#include <fstream>      // read file
#include <vector>

#include "board.h"

using namespace std;

int main(int argc, char **argv)
{
    cout << "Enter of sudoku grid or file!" << endl;
    string line;
    ifstream file (argv[1]);

    vector<int> v1(1,5);

    if (file.is_open())
    {
        while (getline(file, line))
        {
            cout << line << '\n';
        }
        file.close();
    }


    //test board = new board();


    return 0;
}

