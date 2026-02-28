#include <iostream>
using namespace std;

int main() {
    int a, b;
    while ( !(cin >> a >> b).eof()) {
        cout << a + b << "\n";
    }

    return 0;
}

/*
#include <iostream>
using namespace std;
int main() {
    int a, b;
    while (cin >> a >> b) {
        cout << a + b << "\n";
    }

    return 0;
}
*/