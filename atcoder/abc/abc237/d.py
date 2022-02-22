from collections import deque
n = int(input())
S = list(input())

q = deque([n])

for i in range(n)[::-1]:
    if S[i] == "R":
        q.appendleft(i)
    else:
        q.append(i)
print(*q)