#include <iostream>
using namespace std;

int main()
{
    string strs[5];
    int maxLength = 0;
    for (int i = 0; i < 5; i++)
    {
        cin >> strs[i];
        if (strs[i].length() > maxLength)
        {
            maxLength = strs[i].length();
        }
    }


    for (int i = 0; i < maxLength; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (i >= strs[j].length())
                continue;
            cout << strs[j][i];
        }
    }
}