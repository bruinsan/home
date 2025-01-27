#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdlib> // std::atoi

bool checkReport(const std::string& reportLevels)
{
    std::stringstream ss(reportLevels);
    std::string level;

    std::getline(ss, level, ' '); 
    int currentReport = std::atoi(level.c_str());
    // std::cout << currentReport << " ";

    std::getline(ss, level, ' ');
    int nextReport = std::atoi(level.c_str());
    // std::cout << nextReport << " ";

    int baseDiff = currentReport - nextReport;
    int baseSignal = (baseDiff) > 0 ? 1 : -1;
    if (std::abs(baseDiff) > 3 || baseDiff == 0) return false;

    while (std::getline(ss, level, ' '))
    {
        int diff = nextReport - std::atoi(level.c_str());

        int signal = diff > 0 ? 1 : -1;
        if (signal != baseSignal) return false;

        if (std::abs(diff) > 3 || diff == 0) return false;

        nextReport = std::atoi(level.c_str());
        // std::cout << nextReport << " ";
        
        // int diff = std::abs(currentReport - std::atoi(level.c_str()));
        // // get the signal (increasing or decreasing)
        // std::cout << diff << " ";
        // if (diff > 3)
        // {
        //     reportSafe = false;
        // }
        // currentReport = std::atoi(level.c_str());

    }
    // std::cout << "\n";
    std::cout << "report Safe" << std::endl;
    return true;
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
            std::cout << ++line << " ";
            // call check report
            if (checkReport(ln))
            {
                safeRpCount++;
            }
            else
            {
                std::cout << "\n";
            }

        }
        file.close();
    }
    std::cout << safeRpCount << std::endl;

    return 0;
}

