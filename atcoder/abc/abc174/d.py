n = int(input())
c = list(input())

l = 0
r = n-1
count = 0
while r > l:
    while r >= 0 and c[r] != "R":
        r -= 1
    while l < n and c[l] != "W":
        l += 1
    
    if r < 0 or l >= n:
        break
    elif r < l:
        break
    else:
        count += 1
        r -= 1
        l += 1
    
print(count)