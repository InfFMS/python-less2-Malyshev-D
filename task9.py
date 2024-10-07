a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if abs(a2 - a1) == 2 and abs(b2 - b1) == 1:
    print('YES')
if abs(a2 - a1) == 1 and abs(b2 - b1) == 2:
    print('YES')
else: print('NO')