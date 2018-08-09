#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>

uint64_t sum_multiple_3_5(int nb)
{
    uint64_t sum = 0;
    for(int i=3 ; i<nb ; i++)
    {
        if(i%3 == 0)
        {
            sum += i;
        }
        else{
            if(i%5 ==0)
            {
                sum += i;
            }
        }
    }
    return sum;
}

uint64_t vector_sum(std::vector<uint64_t> vec)
{
    uint64_t sum_elems = 0;
    for(auto& n : vec) sum_elems += n;
    return sum_elems;
}

uint64_t quick_master_3_5(int nb)
{
    float mul_3 = (nb-1)/3;
    float mul_5 = (nb-1)/5;
    float mul_15 = (nb-1)/15;

    float mmm3 = mul_3 * 3;
    float mmm5 = mul_5 * 5;
    float mmm15 = mul_15 * 15;

    float sum = 0;
    
//    uint64_t mul_3 = (nb-1)/3;
//    uint64_t mul_5 = (nb-1)/5;
//    uint64_t mul_15 = (nb-1)/15;
//
//    uint64_t mmm3 = mul_3 * 3;
//    uint64_t mmm5 = mul_5 * 5;
//    uint64_t mmm15 = mul_15 * 15;
//
//    uint64_t sum = 0;

    sum += ((3 + mmm3) / 2) * mul_3;
    //std::cout << sum << std::endl;
    sum += ((5 + mmm5) / 2) * mul_5;
    sum -= ((15 + mmm15) / 2) * mul_15;

    return sum;

}


int main()
{
    int howMany;
    std::vector<int> vec_nb;
    std::cin >> howMany;
    
    for(int i = 0 ; i < howMany ; i++)
    {
        int temp_seq;
        std::cin >> temp_seq;
        vec_nb.push_back(temp_seq);
    }

    std::vector<int>::iterator it;

    for(it = vec_nb.begin() ; it != vec_nb.end() ; it++)
    { 
      //    std::cout << sum_multiple_3_5(*it) << std::endl;
      //  std::cout << "quick calculus" << std::endl;
//        std::cout << quick_multiple_3_5(*it) << std::endl;
          std::cout << quick_master_3_5(*it) << std::endl;
    }

    return 0;
}
