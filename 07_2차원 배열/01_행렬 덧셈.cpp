#include <iostream>
using namespace std;

int main()
{
    int N, M, tmp;
    int firstArr[100][100];
    // int secondArr[100][100];
    cin >> N >> M;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> firstArr[i][j];
        }
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> tmp;
            cout << firstArr[i][j] + tmp << " ";
        }
        cout << "\n";
    }

    return 0;
}