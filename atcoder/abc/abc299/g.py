from heapq import heappop,heappush

n,m = map(int,input().split())
A = list(map(int,input().split()))

nums = [0]*(m+1)
for a in A:
    nums[a] += 1

ans = []
used = [0]*(m+1)
last = -1

mod = (1<<20)

h = []
for i,a in enumerate(A):

    if used[a]:
        continue

    nums[a] -= 1

    heappush(h,(a<<20)+i)
    if nums[a]:
        continue

    while h and used[a] == 0:
        top,ind = divmod(heappop(h),mod)
        if ind < last:
            continue
        if used[top]:
            continue
        used[top] = 1
        last = ind
        ans.append(top)

print(*ans)
    
