t = int(input())
for _ in range(t):
    n,l,r,s = map(int,input().split())
    size = r-l+1
    mi = size*(size+1)//2
    ma = n*(n+1)//2-(n-size)*(n-size+1)//2

    if  s < mi or ma < s:
        print(-1)
        continue

    need = [i+1 for i in range(size)]
    cost = sum(need)
    now = size-1
    use = 0
    while cost != s:
        add = n-use-need[now]
        if cost + add <= s:
            need[now] = n-use
            cost += add
            now -= 1
            use += 1
            continue
        need[now] += (s-cost)
        cost = s

    use = [0]*(n+1)
    ans = [0]*(n)
    for i in range(size):
        ans[l-1+i] = need[i]
        use[need[i]] = 1
    now = 1
    for i in range(n):
        if ans[i] != 0:
            continue
        while use[now]:
            now += 1
        ans[i] = now
        use[now] = 1
    print(*ans)

