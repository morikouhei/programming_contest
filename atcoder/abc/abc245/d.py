n,m = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))

B = []
for i in range(m+1):
    c = C[-1]
    a = A[-1]
    dif = c//a
    B.append(dif)
    for j in range(n+1):
        C[-1-j] -= A[-1-j]*dif
    C.pop()
print(*B[::-1])