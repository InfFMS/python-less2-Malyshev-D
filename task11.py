a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if (a2 > b1) and (a2 < b2):
    print(a2-b1)
elif (a2 > b1) and (a2 > b2):
    print(b2-b1)
elif a2 == b1:
    print(a2)
else: print('Пустое множество')