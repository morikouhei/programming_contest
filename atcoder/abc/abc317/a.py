n,h,x = map(int,input().split())
P = list(map(int,input().split()))
for i,p in enumerate(P,1):
    if p+h >= x:
        print(i)
        exit()