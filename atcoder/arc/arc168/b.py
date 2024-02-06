from collections import Counter
n = int(input())
A = list(map(int,input().split()))
C = Counter(A)
A.sort()
xor = 0
for a in A:
    xor ^= a

if xor:
    print(-1)
    exit()


rest = [0]
for key,value in C.items():
    if value%2:
        rest.append(key)

rest.sort()
ans = rest[-1]-1

if ans == -1:
    ans = 0
print(ans)