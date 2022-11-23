n,q = map(int,input().split())
A = [list(map(int,input().split())) for i in range(n)]

for _ in range(q):
    s,t = map(int,input().split())
    print(A[s-1][t])