#include <iostream>
using namespace std;

int main()
{
    string subject, grade;
    float credit, gradeScore, sumCredit = 0, temp = 0;

    for (int i = 0; i < 20; i++)
    {
        cin >> subject >> credit >> grade;
        if (grade[0] == 'F')
        {
            sumCredit += credit;
            continue;
        }
        else if (grade[0] == 'P')
            continue;
        else if (grade[0] == 'A')
            gradeScore = 4.0;
        else if (grade[0] == 'B')
            gradeScore = 3.0;
        else if (grade[0] == 'C')
            gradeScore = 2.0;
        else
            gradeScore = 1.0;
        if (grade[1] == '+')
            gradeScore += 0.5;

        sumCredit += credit;
        temp += gradeScore * credit;
    }

    cout << temp / sumCredit;

    return 0;
}