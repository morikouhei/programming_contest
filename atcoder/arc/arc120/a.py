n = int(input())
A = list(map(int,input().split()))

m = 0
cum = 0
s = 0
for i in range(n):
    m = max(m,A[i])
    s += A[i]
    print(s+cum+m*(i+1))
    cum += s
