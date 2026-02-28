// #include <iostream>
// using namespace std;

// int main()
// {
//     int N, M, i, j, tmp;
//     int basket[101];

//     cin >> N >> M;

//     for (int k = 1; k <= N; k++)
//     {
//         basket[k] = k;
//     }

//     for (int k = 0; k < M; k++)
//     {
//         cin >> i >> j;
//         while (i < j)
//         {
//             tmp = basket[j];
//             basket[j] = basket[i];
//             basket[i] = tmp;
//             i++;
//             j--;
//         }
//     }

//     for (int k = 1; k <= N; k++)
//     {
//         cout << basket[k] << " ";
//     }

//     return 0;
// }

// swap 함수 사용
#include <iostream>
using namespace std;

int main()
{
    int N, M, i, j; // tmp 필요 없음

    cin >> N >> M;
    int basket[100];

    for (int k = 1; k <= N; k++)
    {
        basket[k] = k;
    }

    for (int k = 0; k < M; k++)
    {
        cin >> i >> j;
        while (i < j)
        {
            swap(basket[i], basket[j]);
            i++;
            j--;
        }
    }

    for (int k = 1; k <= N; k++)
    {
        cout << basket[k] << " ";
    }

    return 0;
}
