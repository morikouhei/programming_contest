s = input()
n = len(s)
ans = n+1
for i in range(1,1<<n):
    count = 0
    for j in range(n):
        if i >> j & 1:
            count += int(s[j])%3
    if count%3 == 0:
        ans = min(ans,n-bin(i).count("1"))
if ans == n+1:
    ans = -1
print(ans)