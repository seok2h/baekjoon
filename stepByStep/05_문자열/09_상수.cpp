#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    string A, B, result;
    cin >> A >> B;

    for (int i = 2; i >= 0; i--)
    {
        if (A[i] > B[i])
        {
            result = A;
            break;
        }
        else if (A[i] < B[i])
        {
            result = B;
            break;
        }
    }

    for (int i = 2; i >= 0; i--)
    {
        cout << result[i];
    }

    return 0;
}