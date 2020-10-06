from collections import defaultdict
d = defaultdict(int)
d[(0,0)] = 1
n,s = input().split()
n = int(n)
ans = 0
at = 0
gc = 0
for i in s:
    if i == "A":
        at += 1
    elif i == "T":
        at -= 1
    elif i == "G":
        gc += 1
    else:
        gc -= 1
    ans += d[(at,gc)]
    d[(at,gc)] += 1
print(ans)