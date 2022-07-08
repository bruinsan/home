#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
		int i = 0, j = nums.size();
		int h = -1;
		while (i < j)
		{
			h = ((j - i) / 2) + i;
			if (nums[h] == target) return h;

			if (nums[h] > target) j = h;
			else i = h+1;
		}
		return -1;
    }
};

int main(int argc, char** argv)
{
  Solution s;

  std::vector<int> v = {0, 3, 5, 9, 12};
  int out = s.search(v, stoi(argv[1]));
  std::cout << out << std::endl;

  return 0;
}
