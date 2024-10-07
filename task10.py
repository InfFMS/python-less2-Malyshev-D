a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if abs(b2 - b1) % abs(a2 - a1) == 0:
    print('YES')
elif b2 - b1 == 0 and a2 - a1 != 0:
    print('YES')
elif b2 - b1 != 0 and a2 - a1 == 0:
    print('YES')
else: print('NO')