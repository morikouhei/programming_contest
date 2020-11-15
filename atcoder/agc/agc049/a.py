n = int(input())
s = [[int(i) for i in input()]for j in range(n)]
for i in range(n):
    s[i][i] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if s[i][k] and s[k][j]:
                s[i][j] = 1

count = [0]*n
for i in range(n):
    for j in range(n):
        count[j] += s[i][j]

ans = 0
for i in count:
    ans += 1/i
print(ans)