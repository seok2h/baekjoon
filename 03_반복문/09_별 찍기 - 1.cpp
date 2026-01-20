#include <iostream>
using namespace std;

int main()
{
    int N;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j <= i; j++)
            cout << "*";
        cout << "\n";
    }

    return 0;
}

// stdio와 끊어서 하는 법 (속도 향상)
/*
#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);

    int N;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j <= i; j++)
            cout << "*";
        cout << "\n";
    }

    return 0;

}

*/