#include <iostream>
using namespace std;

int main() {
    int a, b, v, days;
    cin >> a >> b >> v;

    if (((v-a) % (a-b)) > 0)
        days = (v-a) / (a-b) + 2;
    else
        days = (v-a) / (a-b) + 1;

    cout << days;

    return 0;
}