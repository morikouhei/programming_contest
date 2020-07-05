t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    
    if k%n:
        print(2)
    else:
        print(0)
    ans = [[0]*n for i in range(n)]
    now = 0
    count = 0
    i = 0
    while count < k:
        if now < n:
            ans[now][(now+i)%n] = 1
            now += 1
            count += 1
        else:
            now = 0
            i += 1
        
    for i in ans:
        print(*i,sep="") 