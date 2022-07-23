# n,k = map(int,input().split())
n,k = 10,2
import itertools

ans = []

for l in itertools.permutations(range(1,n+1),n):

    ok = 1
    for i,x in enumerate(l,1):
        if abs(x-i) < k:
            ok = 0
    if ok:
        ans.append(l)
ans.sort()
print(len(ans))
for i in ans[:20]:
    print(*i)
