from collections import deque

n = int(input())
q = deque([])
for i in range(n):
    L = [x for x in input().split()]
    if L[0] == "1":
        q.append([L[1],int(L[2])])
    else:
        ans = 0
        l = [0]*26
        count = int(L[1])
        
        while count > 0 and q:
            a,b = q.popleft()
            
            if b > count:
                l[ord(a)-ord("a")] += count
                b -= count
                count = 0
                q.appendleft([a,b])
            else:
                l[ord(a)-ord("a")] += b
                count -= b
        
        for j in l:
            ans += j**2

        print(ans)
        
