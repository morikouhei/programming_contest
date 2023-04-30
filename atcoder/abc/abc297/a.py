n,d = map(int,input().split())
T = list(map(int,input().split()))
for t,nt in zip(T,T[1:]):
    if nt - t <= d:
        print(nt)
        exit()
print(-1)