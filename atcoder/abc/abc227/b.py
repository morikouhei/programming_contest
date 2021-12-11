n = int(input())
S = list(map(int,input().split()))
for i in range(1,1001):
    for j in range(1,1001):
        area = 4*i*j+3*i+3*j
        for k in range(n):
            if S[k] == area:
                S[k] = 0
ans = 0
for s in S:
    if s != 0:
        ans += 1
print(ans)