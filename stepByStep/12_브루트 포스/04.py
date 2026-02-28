
'''
url: https://www.acmicpc.net/problem/1018
제목: 체스판 다시 칠하기
번호: 1018

문제
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

출력
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
'''

M, N = map(int, input().split())

board = []

for i in range(M):
    board.append(list(input()))

y = M - 7
x = N - 7

results = []

for i in range(y):
    for j in range(x):
        # first_color = board[i][j]
        draw1 = 0
        draw2 = 0
        # flag = True
        for a in range(8):
            for b in range(8):
                if a % 2 == 0:
                    if b % 2 == 0:
                        if board[a+i][b+j] != 'B':
                            draw1 += 1
                        else:
                            draw2 += 1
                    elif b % 2 == 1:
                        if board[a+i][b+j] != 'W':
                            draw1 += 1
                        else:
                            draw2 += 1

                else: # a % 2 == 1:
                    if b % 2 == 0:
                        if board[a+i][b+j] != 'W':
                            draw1 += 1
                        else:
                            draw2 += 1
                    elif b % 2 == 1:
                        if board[a+i][b+j] != 'B':
                            draw1 += 1
                        else:
                            draw2 += 1

        results.append(min([draw1, draw2]))

                # print(board[a+i][b+j], flag, end='    ')
            #     if flag:
            #         if board[a+i][b+j] != first_color:
            #             draw += 1
            #         flag = not flag
            #     else:
            #         if board[a+i][b+j] == first_color:
            #             draw += 1
            #         flag = not flag
            # flag = not flag
            # print()

                # if board[i][j] == 'B': # True : 'B' / False : 'W'
                #     if flag:
                #         if board[a+i][b+j] != 'B':
                #             draw += 1
                #             flag = not flag
                #     else:
                #         if board[a+i][b+j] != 'W':
                #             draw += 1
                #             flag = not flag

                # else:
                #     if board[i][j] == 'W': # True : 'B' / False : 'W'
                #         if flag:
                #             if board[a+i][b+j] != 'W':
                #                 draw += 1
                #                 flag = not flag
                #         else:
                #             if board[a+i][b+j] != 'B':
                #                 draw += 1
                #                 flag = not flag
                
                
                # if board[a+i][b+j] == board[a+i][b+j+1]:
                #     draw += 1

                # if b == 6 and a != 7:
                #     if board[a+i][b+j+1] != board[a+i+1][0]:
                #         draw += 1
                #         reverse_flag = True

            # if a != 7:        
            # 	if board[a+i][j] == board[a+i+1][j]:
            #         draw += 1

        # results.append(draw)

print(min(results))


# 1 2 3 4 5 6 7 8 9 10 11
# 0 1 2 3 4 5 6 7 8 9 10
# a a a a a a a a a a a 