from collections import deque
n = int(input())
A = deque(sorted(list(map(int,input().split()))))

ans = 0
while len(A) > 1:
    ans += 1
    r = A.pop()
    l = A[0]
    r %= l
    if r:
        A.appendleft(r)
print(ans)
