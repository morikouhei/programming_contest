n,k = map(int,input().split())
a = list(map(int,input().split()))

for i in range(k):
    b = [0]*(n+1)
    for i in range(n):
        if a[i]:
            b[max(0,i-a[i])] += 1
            b[i] -= 1
            b[i+1] += 1 
            b[min(n,i+a[i]+1)] -= 1
    b[0] += 1
    count = b[0]
    for i in range(1,n):
        b[i] += b[i-1]
        count += b[i]
    a = b[:n]
    if count == n*n:
        print(*a)
        exit()
print(*a)