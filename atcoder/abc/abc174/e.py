n,k = map(int,input().split())
a = list(map(int,input().split()))

l = 0
r = 10**10

while r > l + 1:
    m = (r+l)//2
    count = 0
    for i in a:
        if i <= m:
            continue
        count += (i-1)//m
        
    if count > k:
        l = m
    else:
        r = m
    
print(r)