#include <iostream>
using namespace std;

int main() {
    int n;
    int sum = 0;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        sum += i;
    }

    cout << sum;
}

/*
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    cout << ((n + 1) * n) / 2

    return 0;
}

*/
