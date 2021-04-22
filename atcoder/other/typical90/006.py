from collections import deque
n,k = map(int,input().split())
S = input()
ans = []
cand = deque([])
left = k
for i in range(n):
    s = S[i]
    while cand and s < cand[-1]:
        cand.pop()
    cand.append(s)
    if n-i-left <= 0:
        ans.append(cand.popleft())
        left -= 1
print(*ans,sep="")