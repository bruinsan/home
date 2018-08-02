#include <bits/stdc++.h>

using namespace std;

string timeNbToWord(int minutes)
{
    vector<string> less_twenty = { "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                                   "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
                                   "eighteen", "nineteen" };

    vector<string> more_twenty = { "twenty", "thirty", "fourty", "fifty"};
    
    if (minutes < 20)
    {
        return less_twenty[minutes - 1];
    }
    else
    {
        return more_twenty[minutes/10 - 2] + " " + less_twenty[minutes%10 - 1];
    }
}

// Complete the timeInWords function below.
string timeInWords(int h, int m) {
    /*
    o' clock
    past
    to
    */
    
    if(m == 0)
    { 
        return timeNbToWord(h) + " o' clock";
    }
    else{
        if(m <= 30)
        {
            return timeNbToWord(m) + " past " + timeNbToWord(h);
        }else{
            return timeNbToWord(60-m) + " to " + timeNbToWord(h+1);
        }
    }
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

