#include <iostream>
using namespace std;

int main()
{
    int h, m;
    cin >> h >> m;

    if (m - 45 < 0)
    {
        m = 60 + (m - 45);
        if (h - 1 < 0)
        {
            h = 23;
        }
        else
        {
            h--;
        }
    }
    else
    {
        m = m - 45;
    }

    cout << h << " " << m;

    return 0;
}

/*
#include <iostream>
using namespace std;
int main() {
    int a, b;
    cin >> a >> b;
    if (b < 45) {
        b += 15;
        a--;
    }
    else
        b -= 45;
    if (a < 0) a = 23;
    cout << a << " " << b;
}

*/
