#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    string number;
    int n, result = 0;
    cin >> number >> n;
    for (int i = 0; i < number.length(); i++)
    {
        if (number[i] >= '0' && number[i] <= '9')
        {
            result += (number[i] - '0') * pow(n, number.length() - i - 1);
        }
        else
        {
            result += (number[i] - 'A' + 10) * pow(n, number.length() - i - 1);
        }
    }

    cout << result;

    return 0;
}