k = int(input())
ans = 0
for i in range(1,10**5):
    if i**3 > k:
        break
    if k%i:
        continue
    k2 = k//i
    for j in range(i,int(k2**0,5)+1):
        if k2%j:
            continue
        if j <= k2//j:
            ans += 1
print(ans)