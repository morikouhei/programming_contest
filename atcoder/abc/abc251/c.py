n = int(input())
L = []
use = set()
for i in range(n):
    s,t = input().split()
    t = int(t)
    if s in use:
        continue
    use.add(s)
    L.append([s,t,i])
L.sort(key=lambda x: -x[1])

print(L[0][-1]+1)