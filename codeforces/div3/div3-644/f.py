import copy
t = int(input())
al = list("abcdefghijklmnopqrstuvwxyz")
for _ in range(t):
    n,m = map(int,input().split())
    l = [list(input()) for i in range(n)]
    d = l[0]
    do = 0
    for i in range(m):
        c = copy.deepcopy(d)
        for j in range(26):
            c[i] = al[j]
            check = True
            for k in l:
                count = 0
                for r in range(m):
                    if c[r] != k[r]:
                        count += 1
                if count > 1:
                    check = False
                    break
            if check:
                
                do = 1
                ans = copy.deepcopy(c)
    if do:
        print(*ans,sep="")
    else:
        print(-1)

