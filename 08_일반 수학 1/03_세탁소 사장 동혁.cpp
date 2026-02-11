#include <iostream>
using namespace std;

int main()
{
    int T, C, tmp;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        int quarter = 0, dime = 0, nickel = 0, penny = 0;
        cin >> C;
        if (C >= 25)
        {
            quarter = C / 25;
            C %= 25;
        }
        if (C >= 10)
        {
            dime = C / 10;
            C %= 10;
        }
        if (C >= 5)
        {
            nickel = C / 5;
            C %= 5;
        }
        penny = C;
        printf("%d %d %d %d\n", quarter, dime, nickel, penny);
    }

    return 0;
}