#include <iostream>
using namespace std;

int main()
{
    int N;
    int currN = 2;

    cin >> N;

    for (int i = 0; i < N; i++)
        currN = currN + currN - 1;

    cout << currN * currN;

    return 0;
}