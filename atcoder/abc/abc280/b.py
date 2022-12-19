n = int(input())
S = list(map(int,input().split()))
A = [0]
cum = 0
for s in S:
    dif = s-cum
    A.append(dif)
    cum += dif
print(*A[1:])