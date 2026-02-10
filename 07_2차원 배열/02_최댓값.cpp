#include <iostream>
using namespace std;

int main()
{
    int max = -1;
    int tmp, max_index;
    for (int i = 0; i < 81; i++)
    {
        cin >> tmp;
        if (max < tmp)
        {
            max = tmp;
            max_index = i;
        }
    }

    cout << max << "\n";
    cout << max_index / 9 + 1 << " " << max_index % 9 + 1;

    return 0;
}
