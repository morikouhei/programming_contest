from collections import deque
S = input()
q = deque([])
turn = 0
for s in S:
    if s == "R":
        turn ^= 1
    else:
        if turn:
            q.appendleft(s)
        else:
            q.append(s)

ans = []
if turn:
    while q:
        ans.append(q.pop())
        if len(ans) > 1 and ans[-1] == ans[-2]:
            ans.pop()
            ans.pop()
else:
    while q:
        ans.append(q.popleft())
        if len(ans) > 1 and ans[-1] == ans[-2]:
            ans.pop()
            ans.pop()

print(*ans,sep="")