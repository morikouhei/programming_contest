n,m = map(int,input().split())
R = []
for i in range(m):
    k = int(input())
    R.append([int(x)-1 for x in input().split()])

id = [[] for i in range(n)]
for i,r in enumerate(R):
    for j in r:
        id[j].append(i)

num = [[] for i in range(n)]
num[0].append(0)
use = [0]*m
ans = [-1]*n
ans[0] = 0
for i in range(n):
    for j in num[i]:
        for k in id[j]:
            if use[k]:
                continue
            use[k] = 1
            for r in R[k]:
                if ans[r] != -1:
                    continue
                num[i+1].append(r)
                ans[r] = i+1

for i in ans:
    print(i)

