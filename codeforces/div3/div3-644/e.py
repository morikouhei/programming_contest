t = int(input())
for _ in range(t):
    n = int(input())
    l = [list(input()) for i in range(n)]
    check = True
    for i in range(n):
        for j in range(n):
            if l[i][j] == "1":
                if i == n-1:
                    continue
                if j == n-1:
                    continue
                if l[i+1][j] == "1" or l[i][j+1] == "1":
                    continue
                check = False
                break
    if check:
        print("YES")
    else:
        print("NO")