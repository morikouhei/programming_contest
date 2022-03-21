import sys

n = int(input())
M = 2*n+1
used = [0]*(M+1)

for i in range(n+1):
    for j in range(1,M+1):
        if used[j]:
            continue
        used[j] = 1
        print(j)
        sys.stdout.flush()
        used[int(input())] = 1

    