import bisect
n,q = map(int,input().split())
A = sorted(list(map(int,input().split())))

for i in range(q):
    x = int(input())
    print(n-bisect.bisect_left(A,x))