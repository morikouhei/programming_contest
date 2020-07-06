N,X = map(int,input().split())
L = list(map(int,input().split()))
ans = 1
d = 0
for l in L:
    d += l
    if X >= d:
        ans += 1
print(ans)