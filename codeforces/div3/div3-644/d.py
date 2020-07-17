t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    ans = float("INF")
    for i in range(1,int(n**0.5)+5):
        if i > k:
            break
        if n%i == 0:
            x = n//i
            ans = min(ans,x)
            if x <= k:
                ans = min(ans,i)
    print(ans)
            
            