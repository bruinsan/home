#include <iostream>
#include <vector>


using namespace std;

class Solution {
public:

    void printVector(vector<int>& v)
    {
	    for (const int& i : v)
	    {
		    cout << i << " ";
	    }
	    cout << endl;
    }

    vector<int> sortedSquares(vector<int>& nums) {
        // -4, -1, 0, 3, 10 --> 16, 1, 0, 9, 100
        
        vector<int> neg, pos;
        
        for (const int& i : nums)
        {
            if (i >= 0) pos.push_back(i*i);
            else neg.push_back(i*i);
        }
        
        vector<int> out;
        
        int limit = min(pos.size(), neg.size());
        
        int i_pos = 0, j_neg = neg.size() - 1;
        printVector(pos); printVector(neg); 
        while(i_pos < pos.size() && j_neg > 0)
        {
            if (pos[i_pos] >= neg[j_neg])
            {
                out.push_back(neg[j_neg]);
                j_neg--;
            }
            else
            {
                out.push_back(pos[i_pos]);
                i_pos++;
            }
        }
        cout << "i = " << i_pos << " j = " << j_neg << endl;
	printVector(out);	
        if (i_pos == pos.size()-1)
        {
            // add the rest of neg
            while (j_neg >= 0)
            {
                out.push_back(neg[j_neg]);
                j_neg--;
            }
        }
        else
        {
            // add the rest of pos   
            while (i_pos < pos.size())
            {
                out.push_back(pos[i_pos]);
                i_pos++;
            }
        }
        
        return out;
    }
};

int main()
{
	Solution s;

	vector<int> v = {-4,-1,0,3,10};
	vector<int> ans = s.sortedSquares(v);
	
	s.printVector(ans);
	
	return 0;
}
