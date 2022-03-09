n,k = map(int,input().split())
A = list(map(int,input().split()))

m = 55
double = [[0]*n for i in range(m)]

for i,a in enumerate(A):
    double[0][i] = a


for i in range(m-1):
    for j in range(n):
        double[i+1][j] = double[i][j]+double[i][(double[i][j]+j)%n]


ans = 0
ind = 0
for i in range(m)[::-1]:
    if k >> i & 1:
        ans += double[i][ind]
        ind = ans%n

print(ans)
