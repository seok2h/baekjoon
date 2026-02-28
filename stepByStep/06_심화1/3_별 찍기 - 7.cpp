#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int space = n - 1, star = 1;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < space; j++)
        {
            cout << " ";
        }
        for (int k = 0; k < star; k++)
        {
            cout << "*";
        }
        cout << "\n";
        space--, star += 2;
    }

    space = 1, star = n * 2 - 3;
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < space; j++)
        {
            cout << " ";
        }
        for (int k = 0; k < star; k++)
        {
            cout << "*";
        }
        cout << "\n";
        space++, star -= 2;
    }
    
    return 0;
}