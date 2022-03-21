from collections import deque
n,x = map(int,input().split())
q = deque([])
s = ""
now = x
while now:
    if now&1:
        s += "1"
    else:
        s += "0"
    now //= 2
s = s[::-1]
for i in s:
    q.append(int(i))
S = input()
for s in S:
    if s == "U":
        q.pop()
    if s == "L":
        q.append(0)
    if s == "R":
        q.append(1)

ans = 0
for i in q:
    ans *= 2
    ans += i
print(ans)