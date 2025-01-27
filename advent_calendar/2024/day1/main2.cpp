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
    std::unordered_map<std::string, int> nb_count;

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

    // count A appearences in B
    for (const std::string& nbA : vA)
    {
        if (nb_count.find(nbA) == nb_count.end())   // still not in the nb_count
        {
            for (std::string& nbB : vB)
            {
                if (nbA == nbB)
                {
                    nb_count[nbA]++;
                }
            }
        }
    }

    // std::cout << "32705 = " << nb_count["32705"] << std::endl;

    int sum = 0;
    for (const auto& nb : nb_count)
    {
        sum += std::atoi(nb.first.c_str()) * nb.second;
    }

    std::cout << sum << std::endl;


    
    return 0;
}

