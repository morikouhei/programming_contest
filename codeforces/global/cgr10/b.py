t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    if k%2:
        x = max(a)
        for j in range(n):
            a[j] = x-a[j]
        print(*a) 
    else:
        for i in range(2):
            x = max(a)
            for j in range(n):
                a[j] = x-a[j]
        print(*a)