#include <iostream>
using namespace std;

int main()
{
    int numberOfStudent;
    int student[31] = {
        0,
    };
    for (int i = 0; i < 28; i++)
    {
        cin >> numberOfStudent;
        student[numberOfStudent] = 1;
    }

    for (int i = 1; i <= 30; i++)
    {
        if (student[i] == 0)
        {
            cout << i << "\n";
        }
    }

    return 0;
}