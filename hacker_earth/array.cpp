#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int i, N;
    cin >> N;
    vector<int> A(N), B(N);
    
    for (i=0 ; i<N ; i++)
    {
        cin >> A[i];
	cout << "A[" << i << "] = " << A[i] << endl;
    }
    
    for (i=0 ; i<N ; i++)
    {
        cout << A[i];
    }
    cout << endl;
}

