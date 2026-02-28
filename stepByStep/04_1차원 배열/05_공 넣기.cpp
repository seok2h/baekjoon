#include <iostream>
using namespace std;

int main()
{
    int numberOfBasket, cnt;
    int startIndex, endIndex, ball;
    int basket[100] = {
        0,
    };
    cin >> numberOfBasket >> cnt;

    for (int i = 0; i < cnt; i++)
    {
        cin >> startIndex >> endIndex >> ball;
        for (int j = startIndex; j <= endIndex; j++)
        {
            basket[j] = ball;
        }
    }

    for (int k = 1; k <= numberOfBasket; k++)
    {
        cout << basket[k] << " ";
    }

    return 0;
}