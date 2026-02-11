#include <iostream>
using namespace std;

int main()
{
    int a, b, num, line = 1;
    cin >> num;

    while (num > line)
    {
        num -= line;
        line += 1;
    }

    if (line % 2 == 0)
    {
        a = num;
        b = line - num + 1;
    }
    else
    {
        a = line - num + 1;
        b = num;
    }

    cout << a << "/" << b;

    return 0;
}