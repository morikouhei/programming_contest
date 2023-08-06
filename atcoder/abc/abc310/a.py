n,p,q = map(int,input().split())
D = list(map(int,input().split()))
print(min(p,min(D)+q))