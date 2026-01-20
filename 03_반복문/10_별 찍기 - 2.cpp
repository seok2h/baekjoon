#include <iostream>
using namespace std;

int main()
{
    int N;
    cin >> N;
    int j = 0, k = N - 1;
    for (int i = 0; i < N; i++)
    {
        for (j = 0; j < k; j++)
        {
            cout << " ";
        }
        for (; j < N; j++)
        {
            cout << "*";
        }
        k--;
        cout << "\n";
    }

    return 0;
}

/*
#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    for (int row = 1; row <= N; row++) {
        for (int i = 0; i < N - row; i++) {
            cout << " "
        }

        for (int i = 0; i < row; i++) {
            cout << "*";
        }

        cout << "\n";
    }
}
*/