"""
https://www.acmicpc.net/problem/1316
제목 : 그룹 단어 체커
번호 : 1316

문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다.
단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.
"""

num = int(input())
word_list = []
count = 0

for n in range(num):
    word_list.append(input())

for word in word_list:
    char_list = []
    past_char = word[0]
    char_list.append(past_char)
    index = 1
    while index < len(word):
        current_char = word[index]
        if not (current_char in char_list):     # 새로운 알파벳의 등장
            char_list.append(current_char)
            past_char = current_char
            index += 1
        elif current_char == past_char:     # 기존에 있지만 연속적
            index += 1
        else:                               # 기존에 있지만 연속적이지 않음
            break

    if index == len(word):                  # index가 끝까지 감 -> 조건에 만족함
        count += 1


print(count)
