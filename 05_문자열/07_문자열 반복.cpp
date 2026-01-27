#include <iostream>
using namespace std;

int main()
{
    int T, repeat;
    string s;

    cin >> T;
    for (int k = 0; k < T; k++)
    {
        cin >> repeat >> s;
        for (int i = 0; i < s.length(); i++)
        {
            for (int j = 0; j < repeat; j++)
            {
                cout << s[i];
            }
        }
        cout << "\n";
    }

    return 0;
}