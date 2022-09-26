n = int(input())

dp = 3.5
if n == 1:
    print(dp)
    exit()

for i in range(n-1):
    ndp = 0
    for j in range(1,7):
        if j > dp:
            ndp += j
        else:
            ndp += dp
    dp = ndp/6
print(dp)
