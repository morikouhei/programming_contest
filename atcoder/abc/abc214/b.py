s,t = map(int,input().split())
ans = 0
for i in range(s+1):
    for j in range(s+1):
        for k in range(s+1):
            if i+j+k > s:
                continue
            if i*j*k <= t:
                ans += 1
print(ans)