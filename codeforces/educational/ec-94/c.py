t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    x = int(input())
    ans = [1]*n
    check = True
    for i in range(n):
        if s[i] == "0":
            if i-x>= 0:
                ans[i-x] = 0
            if i+x < n:
                ans[i+x] = 0
    for i in range(n):
        if s[i] == "1":
            if (i-x>= 0 and ans[i-x] == 1) or (i+x < n and ans[i+x] == 1):
                continue
            check = False
            break
    if check:
        print(*ans,sep="")
    else:
        print(-1)

