from collections import Counter
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
count = 0
for i in range(n):
    if A[i] == B[i]:
        count += 1

print(count)
ca = Counter(A)
cb = Counter(B)

ans = 0
for k,v in ca.items():
    if k in cb:
        ans += v*cb[k]
print(ans-count)