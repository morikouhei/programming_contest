n = int(input())
A = list(map(int,input().split()))
fmin = min(A[:n])

cand = 10**10
for i in range(n):
    if A[i] == fmin:
        cand = min(cand,A[i+n])

if cand <= fmin:
    print(fmin,cand)
    exit()

used = [0]*n

first = 10**10
second = 10**10
last = -1

ansf = []
ansb = []
for i in range(n):
    if A[i] != fmin:
        continue
    used[i] = 1
    last = i
    ansf.append(A[i])
    ansb.append(A[i+n])

