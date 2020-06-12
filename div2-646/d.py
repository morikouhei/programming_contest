import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    
    n,k = map(int,input().split())
    l = [[] for i in range(k)]
    for i in range(k):
        c,*l[i] = map(int,input().split())
    print("?",n,*list(range(1,n+1)))
    sys.stdout.flush()
    mx = int(input())

    le = 1
    ri = n
    while ri > le:
        m = (ri+le+1)//2
        x = [i for i in range(m,ri+1)]
        print("?",len(x),*x)
        sys.stdout.flush()
        if int(input()) == mx:
            le = m
        else:
            ri = m-1
    ind = ri
    ans = []
    for i in l:
        if ind in i:
            t = set(i)
            x = []
            for j in range(1,n+1):
                if j not in t:
                    x.append(j)
            print("?",len(x),*x)
            sys.stdout.flush()
            ans.append(int(input()))
        else:
            ans.append(mx)
    print("!",*ans)
    sys.stdout.flush()
    x = input()
