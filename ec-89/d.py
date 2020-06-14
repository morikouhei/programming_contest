n = int(input())
a = list(map(int,input().split()))

lm = max(a)+2
x = [-1]*(lm)
for i in range(2,int(lm**0.5)+1):
    if x[i] == -1:
        for j in range(i,lm,i):
            x[j] = i
ans = [[-1]*n for i in range(2)]

for i in range(n):
    c = a[i]
    if x[c] == -1:
        continue
    d = x[c]
    while c%d == 0:
        c //= d
    if c != 1:
        ans[0][i] = c
        ans[1][i] = d
for i in ans:
    print(*i)
