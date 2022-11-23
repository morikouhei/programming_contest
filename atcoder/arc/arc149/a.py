n,m = map(int,input().split())
if m == 10:
    print(-1)
    exit()


base = 0
ten = 1
for i in range(n):
    base += ten
    base %= m
    ten *= 10
    ten %= m

for i in range(n)[::-1]:
    for j in range(1,10)[::-1]:
        if base*j%m == 0:
            print(str(j)*(i+1))
            exit()
    base -= pow(10,i,m)
    base %= m
print(-1)