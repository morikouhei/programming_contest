t = int(input())
for _ in range(t):
    n = int(input())
    l = list(input())
    count = []
    k = 2
    c = 1
    for i in range(30):
        if k <= n:
            count.append([0]*k)
        else:
            break
        k *= 2
        c += 1
    count.append([0]*(k//2))
    if n == 1:
        if l[0] == "a":
            print(0)
        else:
            print(1)
        continue
    for i in range(n):
        x = ord(l[i])-ord("a")
        
        if x >= c:
            continue
        count[x][i*len(count[x])//n] += 1
    ans = n
    
    for i in range(n):
        x = ord(l[i])-ord("a")
        if x >= c:
            continue
        co = 0
        co += count[x][i*len(count[x])//n]
        while x > 0:
            x -= 1
            now = i*len(count[x])//n
            if now %2:
                now -= 1
            else:
                now += 1
        
            co += count[x][now] 
        ans = min(ans,n-co)
    print(ans)    
    