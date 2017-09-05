#include <iostream>
using namespace std;

template <class T>
inline T sum_array (const T* array, int size_array)
{
  T sum = 0;

  for(int i=0; i<size_array; i++)
  {
    sum += array[i];
  }

  return sum;
}

int main()
{
  //int* array = new int[5];
  int array[5] = {1, 2, 3, 4, 5};

  double array2[5] = {1.1, 2.2, 3.3, 4.4, 5.5};

  cout << sum_array(array, 5) << endl;

  cout << sum_array(array2, 5) << endl;

  return 0;
}
