n,m = map(int,input().split())
S = input()
C = list(map(int,input().split()))

l = [[] for i in range(m+1)]
for i,c in enumerate(C):
    l[c].append(i)
ans = [""]*n

for x in l:
    if x == []:
        continue
    ans[x[0]] = S[x[-1]]
    for i,ni in zip(x,x[1:]):
        ans[ni] = S[i]

print(*ans,sep="")