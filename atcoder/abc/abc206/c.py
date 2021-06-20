from collections import Counter
n = int(input())
A = list(map(int,input().split()))
C = Counter(A)
ans = 0
for i,c in C.items():
    ans += c*(n-c)
print(ans//2)