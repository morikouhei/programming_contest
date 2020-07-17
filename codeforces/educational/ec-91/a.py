import bisect
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l2 = [[l[i],i] for i in range(n)]
    l2.sort()
    x = []
    x.append(l2[0][1])
    x.append(l2[1][1])
    x.sort()
    check = True
    for i in range(2,n):
        y = l2[i][1]
        ind = bisect.bisect_left(x,y)
        if ind != 0 and ind != len(x):
            print("YES")
            check = False
            print(x[0]+1,y+1,x[-1]+1)
            break
        else:
            x.insert(ind,y)
    if check:
        print("NO")
    
