n,k = map(int,input().split())
p = list(map(int,input().split()))
l = sorted(p)
print(sum(l[:k]))