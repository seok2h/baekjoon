#include <iostream>
using namespace std;

int main()
{
    int remain[42] = {
        0,
    };
    int input, cnt = 0;
    for (int i = 0; i < 10; i++)
    {
        cin >> input;
        remain[input % 42] = 1;
    }

    for (int i = 0; i <= 41; i++)
    {
        if (remain[i] == 1)
        {
            cnt += 1;
        }
    }

    cout << cnt;

    return 0;
}