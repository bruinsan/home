#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

int findRankPosition(int scr, vector<int> scores)
{
//  int rank = 1;
//
//  if(scr > scores[0])
//  {
//    return rank;
//  }
//  else
//  {
//    for(int i=1 ; i<scores.size() ; i++)
//    {
//      int value = scores[i]
//      
//      if(scr < scores[i])
//      {
//        // compare if the next value is equal or not
//        if(scores[i-1] == scores[i])
//        {
//  	// rank position is the same. eg. 100 100 50 40 40 20 10
//          // rank will not change
//        }
//        else
//        {
//  	rank++;
//        }
//      }
//    }
//  }
  rivalIndex = 0;
  rival = scores[rivalIndex];
  rank = 1;
  rivalRank = 1
  while(scr < rival && rival != scores.last())
  {
    rivalIndex++;
    rival = scores[rivalIndex];

    if (rival == scores[rivalIndex - 1]) 
    {
      // rivalRank doesn't change
    } 
    else{
      rivalRank++;
      rank++;
    }
  }

}

vector<int> climbingLeaderboard(vector<int> scores, vector<int> alice) {
  vector<int> rank(alice.size());
	
  for(int i=0 ; i < alice.size() ; i++)
  {
    rank.push_back(findRankPosition(alice[i], scores) );
  }
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int scores_count;
    cin >> scores_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string scores_temp_temp;
    getline(cin, scores_temp_temp);

    vector<string> scores_temp = split_string(scores_temp_temp);

    vector<int> scores(scores_count);

    for (int scores_itr = 0; scores_itr < scores_count; scores_itr++) {
        int scores_item = stoi(scores_temp[scores_itr]);

        scores[scores_itr] = scores_item;
    }

    int alice_count;
    cin >> alice_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string alice_temp_temp;
    getline(cin, alice_temp_temp);

    vector<string> alice_temp = split_string(alice_temp_temp);

    vector<int> alice(alice_count);

    for (int alice_itr = 0; alice_itr < alice_count; alice_itr++) {
        int alice_item = stoi(alice_temp[alice_itr]);

        alice[alice_itr] = alice_item;
    }

    vector<int> result = climbingLeaderboard(scores, alice);

    for (int result_itr = 0; result_itr < result.size(); result_itr++) {
        fout << result[result_itr];

        if (result_itr != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}

