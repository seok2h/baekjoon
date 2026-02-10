#include <iostream>
using namespace std;

int main()
{
    int basePaper[100][100] = {
        0,
    };
    int nPaper, x, y, totalSpace = 0;
    cin >> nPaper;

    for (int i = 0; i < nPaper; i++)
    {
        cin >> x >> y;
        for (int i = 0; i < 10; i++)
        {
            for (int j = 0; j < 10; j++)
            {
                basePaper[x + i][y + j] += 1;
            }
        }
    }

    for (int i = 0; i < 100; i++)
    {
        for (int j = 0; j < 100; j++)
        {
            if (basePaper[i][j] >= 1)
            {
                totalSpace++;
            }
        }
    }

    cout << totalSpace;

    return 0;
}