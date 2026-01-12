#include <iostream>
#include <cstdlib> // atoi를 사용하기 위함
using namespace std;

int main()
{
    int a;
    char b[4];

    cin >> a;
    cin >> b;

    cout << a * (b[2] - '0') << "\n";
    cout << a * (b[1] - '0') << "\n";
    cout << a * (b[0] - '0') << "\n";
    cout << a * atoi(b) << "\n";

    return 0;
}
