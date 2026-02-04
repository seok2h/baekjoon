#include <iostream>
using namespace std;

int main()
{
    int chess[6] = {1, 1, 2, 2, 2, 8};
    int pieceCounts[6];
    // int king, queen, rook, bishop, knight, pawn;

    cin >> pieceCounts[0] >> pieceCounts[1] >> pieceCounts[2] >> pieceCounts[3] >> pieceCounts[4] >> pieceCounts[5];
    for (int i = 0; i < 6; i++)
    {
        cout << chess[i] - pieceCounts[i] << " ";
    }

    return 0;
}