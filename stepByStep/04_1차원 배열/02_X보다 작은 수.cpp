#include <iostream>
using namespace std;

int main()
{
    int N, X;
    int number;
    cin >> N >> X;

    for (int i = 0; i < N; i++)
    {
        cin >> number;
        if (X > number)
        {
            cout << number << " ";
        }
    }

    return 0;
}