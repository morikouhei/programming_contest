n = int(input())
p = [0]+list(map(int,input().split()))

ind = [0]*(n+1)
for i in range(n+1):
    ind[p[i]] = i

ans = []
use = [0]*(n+1)
for i in range(1,n+1):

    while ind[i] > i and not use[ind[i]-1]:
        use[ind[i]-1] = 1
        ans.append(ind[i]-1)
        ind[i] -= 1
        ind[p[ind[i]]] += 1
        p[ind[i]],p[ind[i]+1] = p[ind[i]+1],p[ind[i]] 
if len(ans) == n-1 and p == [i for i in range(n+1)]:
    for i in ans:
        print(i)
else:
    print(-1)