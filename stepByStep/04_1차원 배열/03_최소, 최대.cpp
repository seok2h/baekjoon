#include <iostream>
using namespace std;

int main()
{
    int N, min = 1000000, max = -1000000;
    int number;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> number;
        if (number < min)
        {
            min = number;
        }
        if (number > max)
        {
            max = number;
        }
    }

    cout << min << " " << max;
    return 0;
}

/* 배열 사용
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;

    int array[1000001];

    for (int i = 0; i < N; i++) {
        cin >> array[i];
    }

    sort(array, array + N);
}
*/