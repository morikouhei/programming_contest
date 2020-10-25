n,m = map(int,input().split())
if m < 0:
    print(-1)
    exit()
if m == 0:
    for i in range(n):
        print(2*i+1,2*i+2)
    exit()
if n-m <= 1:
    print(-1)
    exit()

elif m > 0:
    print(1,10**7-1)
    print(10**7-2,10**7)
    for i in range(1,m+1):
        print(2*i,2*i+1)
    for i in range(n-m-2):
        print(10**7+2*i+1,10**7+2*i+2)
