t = int(input())
from copy import deepcopy

def solve():
    d = [-1]*n
    for i in range(n):
        x,y = l2[i]
        d[y] = i
    ans = []
    count = 0
    for i in range(n-1,1,-1):
        y = d.index(i)
        
        while y < i:
            count += 1
            if y == i-1:
                ans.append(y)
                d[y-1],d[y],d[y+1] = d[y+1],d[y-1],d[y]    
            else:
                ans.append(y+1)
                d[y],d[y+1],d[y+2] = d[y+2],d[y],d[y+1]
            y += 1
    
    if d[0] <= d[1] <= d[2]:
        print(count)
        print(*ans)
        return True
    else:
        check = False
        c = 0
        while c < 3:
            ans.append(1)
            d[0],d[1],d[2] = d[2],d[0],d[1]
            count += 1
            c += 1
            if d[0] <= d[1] <= d[2]:
                check = True
                break
        if check:
            print(count)
            print(*ans)
            return True
        else:
            return False

for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l2 = sorted([[x,i] for i,x in enumerate(l)])

    if solve() == False:
        for i in range(n-1):
            if l2[i][0] == l2[i+1][0]:
                l2[i][1],l2[i+1][1] = l2[i+1][1],l2[i][1]
                break
        if solve() == False:
            print(-1)

    
