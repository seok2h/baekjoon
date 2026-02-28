#include <iostream>
#include <string>
using namespace std;

int main()
{
    int N, cnt = 0;
    string word;
    string tmp;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> word;
        tmp = "";
        tmp += word[0];
        cnt++;
        for (int j = 1; j < word.length(); j++)
        {
            if (tmp.find(word[j]) == string::npos)
            {
                tmp += word[j];
                continue;
            }
            else if ((tmp.find(word[j] != string::npos)) && (word[j] == word[j - 1]))
                continue;
            else
            {
                cnt--;
                break;
            }
        }
    }

    cout << cnt;

    return 0;
}