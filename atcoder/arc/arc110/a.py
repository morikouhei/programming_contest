n = int(input())
now = 1
count = [0]*(n+5)
for i in range(2,n+1):
    now = i
    for j in range(2,now):
        c = 0
        while now%j == 0:
            now //= j
            c += 1
        count[j] = max(count[j],c) 
    if now > 1:
        count[now] = max(count[now],1)
ans = 1
for i in range(2,n+1):
    if count[i]:
        ans *= i**count[i]
ans += 1
print(ans)
