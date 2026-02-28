#include <iostream>
#include <algorithm> // for using std::fill
using namespace std;

int main()
{
    int alphabet[26];
    string input;
    
    fill(alphabet, alphabet + 26, -1); // fill alphabet(arr) with -1

    cin >> input;
    for (int i = 0; i < input.length(); i++)
    {
        if (alphabet[(int)input[i] - (int)'a'] == -1)
        {
            alphabet[(int)input[i] - (int)'a'] = i;
        }
    }

    for (int i = 0; i < 26; i++)
    {
        cout << alphabet[i] << " ";
    }
}