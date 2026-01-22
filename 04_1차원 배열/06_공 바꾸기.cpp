#include <iostream>
using namespace std;

int main()
{
    int N, M, tmp;
    int basket[101] = {
        0,
    };
    int i, j;

    cin >> N >> M;

    for (int k = 1; k <= N; k++)
    {
        basket[k] = k;
    }

    for (int k = 0; k < M; k++)
    {
        cin >> i >> j;
        tmp = basket[i];
        basket[i] = basket[j];
        basket[j] = tmp;
    }

    for (int k = 1; k <= N; k++)
    {
        cout << basket[k] << " ";
    }
}