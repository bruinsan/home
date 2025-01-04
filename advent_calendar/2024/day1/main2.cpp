#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib> // std::atoi
#include <unordered_map>

int main()
{
    std::ifstream file("input");

    // std::vector<std::string> vec = {"4", "2", "7", "3", "6", "0", "-1", "3", "1"};

    // quicksort(vec, 0, vec.size()-1);

    // for (std::string& i : vec)
    // {
    //     std::cout << i << " ";
    // }
    // std::cout << "\n";

    std::vector<std::string> vA;
    std::vector<std::string> vB;

    if (file.is_open())
    {

        std::string strA, strB;
        int nb_lines = 0;
        while (file >> strA >> strB)
        {
            vA.push_back(strA);
            vB.push_back(strB);
            nb_lines++;
        }
        file.close();
    }


    
    return 0;
}

