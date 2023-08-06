n,m = map(int,input().split())
A = [list(map(int,input().split())) for i in range(n)]

ans = 0

mins_lis = [[[1000]*(m+1) for i in range(m)] for j in range(n)]
sums_lis = [[[0]*(m+1) for i in range(m)] for j in range(n)]

for i in range(n):
    for l in range(m):
        mi = A[i][l]
        num = A[i][l]
        for r in range(l+1,m+1):
            mins_lis[i][l][r] = mi
            sums_lis[i][l][r] = num

            if r != m:
                mi = min(mi,A[i][r])
                num += A[i][r]


for l in range(m):
    for r in range(l+1,m+1):
        sums = [sums_lis[i][l][r] for i in range(n)]
        mins = [mins_lis[i][l][r] for i in range(n)]
        q = []
        left = [0]*(n+1)
        mins.append(0)
        sums.append(0)
        for i in range(n+1):
            while q and mins[q[-1]] >= mins[i]:
                t = q.pop()
                ans = max(ans,(sums[i-1] - left[t]) * mins[t])

            sums[i] += sums[i-1]
            left[i] = sums[q[-1]] if q else 0
            q.append(i)
print(ans)