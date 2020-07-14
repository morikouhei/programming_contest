t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    l = [int(i) for i in input().split()]
    l.sort(reverse=True)
    ans = 0
    count = 0
    for i in range(n):
        count += 1
        if count*l[i] >= x:
            ans += 1
            count = 0
    print(ans)
    
