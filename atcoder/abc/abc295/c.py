from collections import Counter
n = int(input())
A = list(map(int,input().split()))
C = Counter(A)
ans = 0

for value in C.values():
    ans += value//2
print(ans)