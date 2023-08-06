n = int(input())
A = list(map(int,input().split()))


ans = 0

i = 0

while i < n:
    if A[i] != 1:
        i += 1
        continue
    
    num = 0
    rows = []

    r = i
    while r < n:
        x = A[r]
        r += 1
        if x == 1:
            num += 1
            rows.append(1)
        else:
            while rows and rows[-1] != x-1:
                rows.pop()
            
            if rows:
                rows[-1] += 1
        
        if rows:
            ans += len(rows)
        else:
            break
    i = r
print(ans)
        