#include <iostream>
using namespace std;

int main()
{
    int n;
    float score, sum = 0, max = 0;
    float scores[1000]; // useless
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> score;
        if (max < score)
        {
            max = score;
        }
        scores[i] = score;
    }

    for (int i = 0; i < n; i++)
    {
        scores[i] = scores[i] / max * 100;
        sum += scores[i];
    }

    cout << sum / n;
}