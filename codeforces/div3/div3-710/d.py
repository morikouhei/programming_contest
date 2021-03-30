from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    C = Counter(A)
    m = C.most_common(1)[0][1]
    print(max(m*2-n,n%2))