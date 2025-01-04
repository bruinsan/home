#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib> // std::atoi


int partition(std::vector<std::string> &vec, int start, int end)
{
    // find a pivot
    int pivot = std::atoi(vec[end].c_str());

    int idxSmaller = start - 1;

    for (int j = start; j <= end - 1; ++j)
    {
        int nb = std::atoi(vec[j].c_str());
        if (nb < pivot)
        {
            idxSmaller++;
            std::swap(vec[idxSmaller], vec[j]);
        }
    }

    std::swap(vec[idxSmaller+1], vec[end]);

    return idxSmaller + 1;
}

void quicksort(std::vector<std::string> &vec, int start, int end)
{
    if (start < end)
    {
        int pIndex = partition(vec, start, end);
        quicksort(vec, start, pIndex - 1);
        quicksort(vec, pIndex + 1, end);
    }
}


int main()
{
    std::ifstream file("input");

    if (file.is_open())
    {
        std::vector<std::string> vA;
        std::vector<std::string> vB;

        std::string strA, strB;
        int nb_lines = 0;
        while (file >> strA >> strB)
        {
            vA.push_back(strA);
            vB.push_back(strB);
            nb_lines++;
        }

        std::cout << "nb_lines = " << nb_lines << std::endl;

        quicksort(vA, 0, vA.size()-1);
        quicksort(vB, 0, vB.size()-1);

        int total_distance = 0;

        for (int i = 0; i < vA.size(); ++i)
        {
            total_distance += std::abs(std::atoi(vA[i].c_str()) - std::atoi(vB[i].c_str()));
        }
        std::cout << "size ordered vec = " << vA.size() << std::endl;
        std::cout << total_distance << std::endl;
    }
    
    return 0;
}

