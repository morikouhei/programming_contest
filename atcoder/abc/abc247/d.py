from collections import deque
q = int(input())

d = deque([])
for _ in range(q):
    l = list(map(int,input().split()))
    if l[0] == 1:
        x,c = l[1:]
        d.append([x,c])

    else:
        c = l[1]
        count = 0
        while c:
            x,nc = d.popleft()
            if c >= nc:
                c -= nc
                count += nc*x
            else:
                count += c*x
                nc -= c
                c = 0
                d.appendleft([x,nc])
        print(count)

