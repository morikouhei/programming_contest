n,q = map(int,input().split())

ans = [i for i in range(n)]
idx = [i for i in range(n)]
for _ in range(q):
    x = int(input())-1
    ind = idx[x]
    if ind < n-1:
        nex = ans[ind+1]
        ans[ind],ans[ind+1] = ans[ind+1],ans[ind]
        idx[x] += 1
        idx[nex] -= 1
    else:
        nex = ans[n-2]
        ans[ind],ans[ind-1] = ans[ind-1],ans[ind]
        idx[x] = n-2
        idx[nex] = n-1

ans = [x+1 for x in ans]
print(*ans)
