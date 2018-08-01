#include <bits/stdc++.h>

using namespace std;

// Complete the timeInWords function below.
string timeInWords(int h, int m) {
    /*
    o' clock
    past
    to
    */
    vector<string> one_ten = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"};
    vector<string> eleven_twenty = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"};
    vector<string> third_fifty = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"};
    
    string whatTimeIs;
    
    if(m == 0)
    { 
        whatTimeIs = "o' clock";
        return one_ten[h] + " " + whatTimeIs;
    }
    else{
        if(m <= 30)
        {
            whatTimeIs = "past"; 
            return minutes + " past " + one_ten[h];
        }else{ 
            whatTimeIs = "to"; 
        }
    }
        
    return whatTimeIs;

    return "eita";
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int h;
    cin >> h;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int m;
    cin >> m;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string result = timeInWords(h, m);
    cout << result << endl;
    fout << result << "\n";

    fout.close();

    return 0;
}

