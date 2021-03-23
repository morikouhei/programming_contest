ans = 0
n = int(input())
for i in range(10**6+5):
    s = str(i)
    s += s
    if int(s) <= n:
        ans += 1
print(ans)