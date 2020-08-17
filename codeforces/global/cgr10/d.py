t = int(input())
for _ in range(t):
    n = int(input())
    l = list(input())
    ans = float("INF")
    for i in range(n):
        if l[i] != l[i-1]:
            
            count = 0
            now = 0
            c = l[i]
            for j in range(n):
                if l[(i+j)%n] == c:
                    now += 1
                else:
                    
                    count += now//3
                    now = 1
                    c = l[(i+j)%n]
            
            count += now//3
            ans = min(ans,count)
            break
    if ans == float("INF"):
        print((n+2)//3)
    else:
        print(ans)
