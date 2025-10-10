#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    void print_vector(std::vector<int>& v)
    {
        for (auto& i : v)
        {
            std::cout << i << " ";
        }
        std::cout << std::endl;
    }

    int removeElement(vector<int>& nums, int val) {
       int i = 0;
       int j = nums.size() - 1;

        if (j < 0) return 0;

       while (i < j)
       {
            if (nums[i] == val) // look for last non val element
            {
                while (j > i)
                {
                    if (nums[j] != val) // swp
                    {
                        // int tmp = nums[j];
                        // nums[j] = nums[i];
                        // nums[i] = tmp;
                        std::swap(nums[i], nums[j]);
                        break;
                    }
                    j--;
                }
            }
            std::cout << i << "  " << j << std::endl;
            print_vector(nums);
            i++;
       }
            std::cout << i << "  " << j << std::endl;
       if (j == 0) return nums.size();
        return j;
    }
};

int main ()
{
    Solution s;

    //std::vector<int> in{3,2,2,3};
    std::vector<int> in{2, 2, 2};
    //std::vector<int> in{0,1,2,2,3,0,4,2};

    std::cout << s.removeElement(in, 3) << std::endl;

    return 0;
}
