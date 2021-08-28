n,k = map(int,input().split())
A = list(map(int,input().split()))

use = [0]*(n+1)
use[0] = 1
for a in A:
    use[a] = 1

lis = []
for i in range(n+1)[::-1]:
    if use[i]:
        continue
    lis.append(i)

ans = []
for i in range(1,k):
    ans.append(A[i-1])
    if lis and A[i-1] > lis[-1]:
        ans.append(lis.pop())
done = 0
for l in lis:
    if l > A[-1]:
        ans.append(l)
    else:
        if done == 0:
            ans.append(A[-1])
            done = 1
        ans.append(l)
if done == 0:
    ans.append(A[-1])
print(*ans)

        