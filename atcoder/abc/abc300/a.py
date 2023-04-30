n,a,b = map(int,input().split())
C = list(map(int,input().split()))
for i,c in enumerate(C):
    if a+b == c:
        print(i+1)