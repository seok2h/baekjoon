#include <iostream>
using namespace std;

int main()
{
    int N;
    int number;
    int target;
    int arr[100] = {
        0,
    };

    for (int i = 0; i < N; i++)
    {
        cin >> number;
        arr[number] += 1;
    }

    cin >> N;
    cin >> target;

    cout << arr[number]; 
}