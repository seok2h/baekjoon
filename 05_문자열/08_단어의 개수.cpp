#include <iostream>
#include <string>
using namespace std;

int main()
{
    string input;
    int cntSpace = 0;
    getline(cin, input);
    for (int i = 0; i < input.length(); i++)
    {
        if (input[i] == ' ')
        {
            cntSpace += 1;
        }
    }

    if (input.length() == 1 && input[0] == ' ')
    {
        cout << 0;
    }
    else
    {
        if (input[0] == ' ')
            cntSpace -= 1;
        if (input[input.length() - 1] == ' ')
            cntSpace -= 1;
        cout << cntSpace + 1;
    }

    return 0;
}

/* cleaner solution
#include <iostream>
#include <sstream>
using namespace std;

int main() {
    string line;
    getline(cin, line);

    string word;
    stringstream ss(line);

    int count = 0;
    while (ss >> word) {
        count++;
    }

    cout << count;
}
*/