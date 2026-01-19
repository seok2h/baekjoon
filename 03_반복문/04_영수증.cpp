#include <iostream>
using namespace std;

int main()
{
    int totalPrice;
    int sum = 0;
    cin >> totalPrice;

    int n;
    cin >> n;

    int price, cnt;
    for (int i = 0; i < n; i++)
    {
        cin >> price >> cnt;
        sum += price * cnt;
    }

    if (sum == totalPrice)
    {
        cout << "Yes";
    }
    else
    {
        cout << "No";
    }
}