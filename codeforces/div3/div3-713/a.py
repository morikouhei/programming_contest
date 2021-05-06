from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    C = Counter(A)
    num = C.most_common()[0][0]

    for i in range(n):
        if num != A[i]:
            print(i+1)
