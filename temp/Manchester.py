
n = int(input())
l = [0]*(2*n-1)
i = 0
j = 0
while i < 2*n - 1:
    while i >= j and i+j+1 < 2*n and a[(i-j)//2] == a[(i+j+1)//2]:
        j += 1
    l[i] = j
    k = 1
    while i + k < 2*n-1 and i >= k and l[i] >= k and l[i-k] != l[i]-k:
        l[i+k] = min(l[i-k],l[i]-k)
        k += 1
    i += k
    if j > k:
        j -= k
    else:
        j = 0