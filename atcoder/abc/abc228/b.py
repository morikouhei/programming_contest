n,x = map(int,input().split())
A = list(map(int,input().split()))
count = [0]*n
count[x-1] = 1
cand = [x-1]
while cand:
    now = cand.pop()

    if count[A[now]-1]:
        continue
    count[A[now]-1] = 1
    cand.append(A[now]-1)
print(sum(count))