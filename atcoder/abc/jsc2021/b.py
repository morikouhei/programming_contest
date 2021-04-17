from collections import Counter
n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ca = Counter(A)
cb = Counter(B)
ans = []
for k,v in ca.items():
    if k in cb:
        continue
    for i in range(v):
        ans.append(k)
for k,v in cb.items():
    if k in ca:
        continue
    for i in range(v):
        ans.append(k)
print(*sorted(ans))