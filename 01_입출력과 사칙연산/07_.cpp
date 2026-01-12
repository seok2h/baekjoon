#include <iostream>
#include <string>

using namespace std;

int main()
{
    string id;
    cin >> id;

    id += "??!";
    cout << id;
}

// string 클래스를 미사용 했을 때
/*
#include <stdio.h>

int main() {
    char id[51]; // 아이디는 알파벳 소문자로만 이루어져 있으며, 길이는 50자를 넘지 않는다.
    scanf("%s", id);
    printf("%s?\?!", id);

    return 0;
}
*/