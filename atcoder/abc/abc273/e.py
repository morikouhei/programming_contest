import sys
input = sys.stdin.readline

q = int(input())

nums = [-1]*(q+1)
par = [0]*(q+1)

memo = {}
ans = [-1]*q
last = 0
now = 0
for i in range(q):
    query = input().split()
    if query[0] == "DELETE":
        now = par[now]
        ans[i] = nums[now]
        continue
    x = int(query[1])

    if query[0] == "ADD":
        last += 1
        nums[last] = x
        par[last] = now
        now = last
        ans[i] = x
    
    elif query[0] == "SAVE":
        memo[x] = now
        ans[i] = nums[now]
    else:
        if x in memo:
            now = memo[x]
        else:
            now = 0
        ans[i] = nums[now]

print(*ans) 
    
        