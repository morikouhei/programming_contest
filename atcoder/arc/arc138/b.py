from collections import deque

n = int(input())
A = list(map(int,input().split()))

q = deque(A)
num = 0
while q:

    while q and (q[-1]+num)%2 == 0:
        q.pop()
    if q:
        if (q[0]+num)%2 == 0:
            q.popleft()
            num ^= 1
        else:
            print("No")
            exit()
print("Yes")