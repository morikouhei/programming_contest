n = int(input())
ans = 0
for i in range(1,n):
    if n//i == n%i:
        ans += i
print(ans)