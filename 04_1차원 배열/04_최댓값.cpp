#include <iostream>
using namespace std;

int main()
{
    int number;
    int max = 0;
    int index = -1;
    for (int i = 0; i < 9; i++)
    {
        cin >> number;
        if (max < number)
        {
            max = number;
            index = i;
        }
    }

    cout << max << "\n";
    cout << index + 1;

    return 0;
}

/* 배열 사용
#include <iostream>
using namespace std;

int main() {
    int num[9];
    for (int i = 0; i < 9; i++) {
        cin >> num[i];
    }

    int maxValue = -1;
    int maxValueIndex;

    for (int i = 0; i < 9; i++) {
        if (num[i] > maxValue) {
            maxValue = num[i];
            maxValueIndex = i;
        }
    }

    cout << maxValue << "\n";
    cout << maxValueIndex + 1;

    return 0;
}
*/