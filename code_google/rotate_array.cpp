#include <iostream>
#include <vector>

using namespace std;

void printVector(const vector<int>& v)
{
	for (const int& i : v)
	{
		cout << i << " ";
	}
	cout << endl;
}


class Solution {
public:
    void rotate(vector<int>& nums, int k) {
				
    }
};

int main()
{
	Solution s;

	vector<int> v = {1,2,3,4,5,6,7};

	s.rotate(v, 3);
	
	printVector(v);
	return 0;
}
