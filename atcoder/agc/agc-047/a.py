import decimal
n = int(input())

cum = [[0]*50 for i in range(50)]

l = []
for i in range(n):
    x = decimal.Decimal(input())
    x *= 10**9
    x = int(x)
    
    two = 0
    while x%2 == 0:
        x //= 2
        two += 1
    five = 0
    while x%5 == 0:
        x //= 5
        five += 1
    cum[two][five] += 1
    l.append((two,five))

for i in range(48,-1,-1):
    for j in range(48,-1,-1):
        cum[i][j] += cum[i][j+1]+cum[i+1][j]-cum[i+1][j+1]

ans = 0
for i,j in l:
    x = max(18-i,0)
    y = max(18-j,0)
    if x <= i and y <= j:
        ans += cum[x][y]-1
    else:
        ans += cum[x][y]
print(ans//2)