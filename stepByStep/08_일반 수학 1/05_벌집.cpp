#include <iostream>
using namespace std;

int main()
{
    int N, i = 1;
    int currN = 1 + (6 * (i - 1));
    cin >> N;

    while (currN < N)
    {
        i++;
        currN = currN + 6 * (i - 1);
    }

    cout << i;

    return 0;
}