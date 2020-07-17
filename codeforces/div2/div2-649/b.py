t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    ans = [l[0]]
    now = 0
    count = l[0]
    for i in l[1:]:
        if now == 0:
            if i > count:
                now = 1
            else:
                now = -1
                
        elif now == 1:
            if i < count:
                ans.append(count)
                now = -1
        elif now == -1:
            if i > count:
                ans.append(count)
                now = 1
        count = i
    ans.append(l[-1])
    print(len(ans))
    print(*ans)