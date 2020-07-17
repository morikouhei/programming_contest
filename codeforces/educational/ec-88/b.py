t = int(input())
for _ in range(t):
    n,m,x,y = map(int,input().split())
    l = [list(input()) for i in range(n)]
    ans = 0
    if x*2 <= y:
        for i in l:
            ans += i.count(".")*x
    else:
        if m == 1:
            for i in l:
                ans += i.count(".")*x
        else:
            for i in range(n):
                for j in range(m-1):
                    if l[i][j] == ".":
                        if l[i][j+1] == ".":
                            ans += y
                            l[i][j] = "#"
                            l[i][j+1] = "#"
                        else:
                            l[i][j] = "#"
                            ans += x
                if l[i][-1] == ".":
                    ans += x
    print(ans)


