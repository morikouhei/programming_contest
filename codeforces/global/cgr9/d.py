t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    ans = []
    count = [0]*(n+1)
    for i in l:
        count[i] += 1
    while True:
        check = True
        for i in range(n):
            if count[i] == 0:
                count[l[i]] -= 1
                count[i] += 1
                ans.append(i+1)
                l[i] = i
                check = False
                break
        if check:
            for i in range(n-1,-1,-1):
                if l[i] != i:
                    count[n] += 1
                    count[l[i]] -= 1
                    l[i] = n
                    ans.append(i+1)
                    check = False
                    break
        if check:
            break
    print(len(ans))
    print(*ans)
