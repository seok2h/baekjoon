s = input()
s = s.split(" ")
A = int(s[0])
B = int(s[1])
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')