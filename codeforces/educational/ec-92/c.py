t = int(input())
for _ in range(t):
    l = [int(i) for i in list(input())]
    ans = float("INF")
    
    for i in range(10):
        for j in range(10):
            count = 0
            now = 1
            for k in l:
                if now == 1:
                    if k != i:
                        count += 1
                    else:
                        now *= -1
                else:
                    if k != j:
                        count += 1
                    else:
                        now *= -1
            if i != j and now == -1:
                count += 1
        
            ans = min(ans,count)
            
    print(ans)