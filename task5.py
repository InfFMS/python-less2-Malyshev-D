a = int(input())
ans = 0
ans += a//100
ans += (a//10)%10 * 10
ans += a%10 * 100
print(ans)