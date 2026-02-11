#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    int num, N, quotient, remainder;
    cin >> num >> N;
    string result;
    quotient = num;
    while (quotient > 0)
    {
        remainder = quotient % N;
        if (remainder < 10)
        {
            result += to_string(remainder);
        }
        else
        {
            result += (char)(55 + remainder);
        }
        quotient /= N;
    }

    reverse(result.begin(), result.end());
    cout << result;

    return 0;
}