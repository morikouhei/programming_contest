import itertools
s,k = input().split()
k = int(k)

ans = set()
n = len(s)
for l in itertools.permutations(range(n)):
    cand = ""
    for j in l:
        cand += s[j]
    ans.add(cand)
ans = sorted(ans)
print(ans[k-1])