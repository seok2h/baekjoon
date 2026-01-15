#include <iostream>
using namespace std;

int main()
{
    int h, m, n;
    cin >> h >> m;
    cin >> n;

    if (m + n > 59)
    {
        h += (m + n) / 60;
        m = (m + n) % 60;
    }
    else
        m += n;
    if (h > 23)
        h -= 24;

    cout << h << " " << m;

    return 0;
}