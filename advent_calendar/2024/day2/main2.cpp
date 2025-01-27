#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdlib> // std::atoi

bool checkReport(const std::string& reportLevels)
{
    int totalLevel = 0;
    int counterBadLevel = 0;
    std::stringstream ss(reportLevels);
    std::string level;

    std::getline(ss, level, ' '); 
    totalLevel++;
    int currentReport = std::atoi(level.c_str());

    std::getline(ss, level, ' ');
    totalLevel++;
    int nextReport = std::atoi(level.c_str());

    int baseDiff = currentReport - nextReport;
    int baseSignal = (baseDiff) > 0 ? 1 : -1;
    if (std::abs(baseDiff) > 3 || baseDiff == 0) counterBadLevel++;

    while (std::getline(ss, level, ' '))
    {
        totalLevel++;
        int diff = nextReport - std::atoi(level.c_str());

        int signal = diff > 0 ? 1 : -1;
        if (signal != baseSignal) counterBadLevel++;

        if (std::abs(diff) > 3 || diff == 0) counterBadLevel++;

        nextReport = std::atoi(level.c_str());
    }

    if (counterBadLevel <= 1)
    {
        std::cout << "safe report" << std::endl;
    }
    else
    {
        std::cout << "unsafe report" << std::endl;
    }

    return (counterBadLevel <= 1) ? true : false;
}


int main()
{
    std::ifstream file("input");
    int line = 0;
    int safeRpCount = 0;

    if (file.is_open())
    {
        std::string ln;    
        while (std::getline(file, ln))
        {
            std::cout << ln << std::endl;
            // std::cout << ++line << " ";
            // call check report
            if (checkReport(ln))
            {
                safeRpCount++;
            }
            // else
            // {
            //     std::cout << "\n";
            // }

        }
        file.close();
    }
    std::cout << safeRpCount << std::endl;

    return 0;
}

