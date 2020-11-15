n = int(input())
s = [int(i) for i in input()]
t = [int(i) for i in input()]

ans = 0
r = 0
for i in range(n):
    if s[i] == t[i]:
        continue
    r = max(r,i+1)
    while r < n and s[r] == 0:
        r += 1
    if r == n:
        print(-1)
        exit()
    ans += r-i
    s[r] = 0
print(ans)
