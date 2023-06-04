S = input()
n = int(input())
le = len(S)
ans = -1

base = 0
for s in S:
    base <<= 1
    if s == "1":
        base += 1

if base > n:
    print(ans)
    exit()


for i,s in enumerate(S):
    if s != "?":
        continue

    if base + (1 << le-i-1) <= n:
        base += 1 << le-i-1
    

print(base)