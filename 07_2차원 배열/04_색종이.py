
'''
url: https://www.acmicpc.net/problem/2563
제목: 색종이
번호: 2563

문제
가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.

예를 들어 흰색 도화지 위에 세 장의 검은색 색종이를 그림과 같은 모양으로 붙였다면 검은색 영역의 넓이는 260이 된다.

입력
첫째 줄에 색종이의 수가 주어진다. 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다. 색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다. 색종이의 수는 100 이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다

출력
첫째 줄에 색종이가 붙은 검은 영역의 넓이를 출력한다.
'''

# 실패작

# position = []
# position_t = []
# area = [] # a ^ b, b ^ c, c ^ a, a ^ b ^ c

# cnt = int(input())

# for i in range(cnt):
#     position.append(map(int, input().split()))

# x = []
# y = []
# for p in position:
#     x.append(p[0])
#     y.append(p[1])

# position_t.append(x)
# position_t.append(y)

# for i in range(cnt):
#     a = i
#     b = a + 1
#     if a == 2:
#         b = 0

#     x_len_diff = abs(position[a][0] - position[b][0])
#     y_len_diff = abs(position[a][1] - position[b][1])
#     if x_len_diff < 10 and y_len_diff < 10:
#         area.append(x_len_diff * y_len_diff)
#     else:
#         area.append(0)

# min_x = min(position_t[0])
# max_x = max(position_t[0])

# min_y = min(position_t[1])
# max_y = max(position_t[1])

# if (max_x - min_x < 10) and (max_y - min_y < 10):

N = int(input())
array = [[0] * 100 for _ in range(100)]  # 도화지 범위 초기화

for _ in range(N):  # 입력 받은 도화지 개수만큼 돈다.
    y1, x1 = map(int, input().split())  # 왼쪽아래 x,y 좌표를 받는다.

    for i in range(x1, x1 + 10):  # 세로를 돈다.
        for j in range(y1, y1 + 10):  # 가로를 돈다.
            array[i][j] = 1  # 해당 범위 값을 0에서 1로 바꿔준다.

result = 0  # 넓이를 출력할 변수
for k in range(100):  # 전체 도화지를 돌면서
    result += array[k].count(1)  # 1 개수만 세어준다

print(result)
