#include <iostream>
using namespace std;

int main()
{
    int alphabet[26] = {
        0,
    };
    int max = 0, max_index;
    bool duplication = false;
    string s;

    cin >> s;

    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] >= 'A' && s[i] <= 'Z')
        {
            alphabet[s[i] - 'A'] += 1;
        }
        if (s[i] >= 'a' && s[i] <= 'z')
        {
            alphabet[s[i] - 'a'] += 1;
        }
    }

    for (int i = 0; i < 26; i++)
    {
        if (max < alphabet[i])
        {
            max = alphabet[i];
            max_index = i;
            duplication = false;
        }
        else if (max == alphabet[i])
        {
            duplication = true;
        }
    }

    if (duplication)
    {
        cout << "?";
    }
    else
    {
        cout << char('A' + max_index);
    }

    return 0;
}
