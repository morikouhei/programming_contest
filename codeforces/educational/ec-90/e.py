t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    ans = float("INF")

    for w in range(17):
        for d in range(10):
            count = 0
            for i in range(k+1):
                if d+i <= 9:
                    count += 9*w + d+i
                else:
                    count += 1+(d+i)-10
            if n >= count and (n-count)%(k+1) == 0:
                s = (n-count)//(k+1)
                if s <= 8:
                    c = str(s)
                else:
                    c = str((s-8)%9)+"9"*((s-8)//9)+"8"
                c += "9"*w
                c += str(d)
                x = int(c)
                
                ans = min(ans,x)

    print(-1 if ans == float("INF") else ans)
