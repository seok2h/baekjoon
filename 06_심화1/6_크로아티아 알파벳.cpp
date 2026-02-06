#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    vector<string> croatian = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
    int index;
    string input;
    cin >> input;

    for (int i = 0; i < croatian.size(); i++)
    {
        while (true)
        {
            index = input.find(croatian[i]);
            if (index == string::npos)
                break;
            input.replace(index, croatian[i].length(), "#");
        }
    }
    cout << input.length();

    return 0;
}