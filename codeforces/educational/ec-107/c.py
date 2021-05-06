n,q = map(int,input().split())
A = list(map(int,input().split()))
T = list(map(int,input().split()))

ind = [0]*(51)
for i,a in enumerate(A,1):
    if ind[a] == 0:
        ind[a] = i
ans = []
for i,t in enumerate(T):
    ans.append(ind[t])
    for j in range(51):
        if ind[j] == 0 or ind[j] >= ind[t]:
            continue
        ind[j] += 1
    ind[t] = 1

print(*ans)

