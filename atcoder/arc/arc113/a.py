k = int(input())

ans = 0
for i in range(1,k+1):
    for j in range(i,k+1):
        if i*j > k:
            break
        for t in range(j,k+1):
            if i*j*t > k:
                break
            if i != j != t:
                ans += 6
            elif i == j == t:
                ans += 1
            else:
                ans += 3
print(ans)