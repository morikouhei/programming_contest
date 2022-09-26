n = int(input())
A = list(map(int,input().split()))
sA = [[len(str(a)),a] for a in A]
sA.sort(reverse=True)

cand = []
for i in range(3):
    cand.append(sA[i][1])

ans = 0
import itertools

for l in itertools.permutations(range(3)):
    base = ""
    for j in l:
        base += str(cand[j])
    ans = max(ans,int(base))
print(ans)