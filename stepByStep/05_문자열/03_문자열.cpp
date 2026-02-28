#include <iostream>
using namespace std;

int main()
{
    int T;
    string input;

    cin >> T;

    for (int i = 0; i < T; i++)
    {
        cin >> input;
        cout << input[0] << input[input.length() - 1] << "\n";
    }
    return 0;
}