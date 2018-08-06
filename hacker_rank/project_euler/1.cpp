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
    uint64_t mul_3 = (nb-1)/3;
    uint64_t mul_5 = (nb-1)/5;
    std::vector<uint64_t> vec_mul;
    for (int i=1 ; i<= mul_3 ; i++)
    {
        vec_mul.push_back(i*3);
    }

    for (int i=1 ; i<= mul_5 ; i++)
    {
        vec_mul.push_back(i*5);
    }
    
    std::cout << vector_sum(vec_mul) << std::endl;
}


//int quick_multiple_3_5(int limit_seq)
//{
//    int multiple = 1;
//    std::vector<int> vec_multiples;
//    vec_multiples.push_back(0);
//    while(vec_multiples.back() < limit_seq)
//    {
////        std::cout << "multiple value --> " << multiple << std::endl;
//        int aux = multiple*3;
//        if(std::find(vec_multiples.begin(), vec_multiples.end(), aux) == vec_multiples.end())
//        {// multiples vector does not have the element, so we push back it
// //           std::cout << "aux value --> " << aux << std::endl;
//            vec_multiples.push_back(aux);
//        }
//    
//        aux = multiple*5;
//        if(std::find(vec_multiples.begin(), vec_multiples.end(), aux) == vec_multiples.end())
//        {// multiples vector does not have the element, so we push back it
// //           std::cout << "aux value --> " << aux << std::endl;
//            vec_multiples.push_back(aux);
//        }
//
//        multiple++;
//    }
//   
//    vec_multiples.pop_back(); // remove last element, it is greater than the limit
//    int aux = multiple*3;
//    if(std::find(vec_multiples.begin(), vec_multiples.end(), aux) == vec_multiples.end())
//    {// multiples vector does not have the element, so we push back it
// //       std::cout << "aux value --> " << aux << std::endl;
//        vec_multiples.push_back(aux);
//    }
////    std::cout << "printing vector" << std::endl;
////    for(std::vector<int>::iterator it = vec_multiples.begin() ; it != vec_multiples.end() ; it++)
////    {
////        std::cout << *it << std::endl;
////    }
////    std::cout << "vector's sum --> " << vector_sum(vec_multiples) << std::endl;
////    return vector_sum(vec_multiples);
//
//}

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
      //  std::cout << sum_multiple_3_5(*it) << std::endl;
      //  std::cout << "quick calculus" << std::endl;
//        std::cout << quick_multiple_3_5(*it) << std::endl;
        quick_master_3_5(*it);
    }

    return 0;
}
