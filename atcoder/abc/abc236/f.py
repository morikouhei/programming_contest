n = int(input())
C = list(map(int,input().split()))

sC = [[c,i+1] for i,c in enumerate(C)]
sC.sort()
vec = []
ans = 0
for c,i in sC:
    for v in vec:
        i = min(i,i^v)
    if i != 0:
        vec.append(i)
        ans += c
print(ans)