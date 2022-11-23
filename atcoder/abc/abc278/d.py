from collections import deque

n = int(input())
A = list(map(int,input().split()))
q = int(input())

event = [deque() for i in range(n)]
for i in range(n):
    event[i].append([-1,A[i]])

last = -2
num = 0
ans = []
for i in range(q):
    l = list(map(int,input().split()))
    if l[0] == 1:
        last = i
        num = l[1]
        continue

    if l[0] == 2:
        ind,x = l[1:]
        event[ind-1].append([i,x])
        continue

    count = num
    ind = l[1]-1
    while event[ind]:
        t,x = event[ind].popleft()
        if t <= last:
            continue
        count += x
    ans.append(count)
    event[ind].append([i,count-num])


for i in ans:
    print(i)