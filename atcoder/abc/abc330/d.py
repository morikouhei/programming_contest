n = int(input())
S = [list(input()) for i in range(n)]

R = [0]*n
C = [0]*n
for i,s in enumerate(S):
    R[i] = s.count("o")

for i in range(n):
    c = 0
    for j in range(n):
        if S[j][i] == "o":
            c += 1
    C[i] = c

ans = 0

for r in range(n):
    for c in range(n):
        if S[r][c] != "o":
            continue
        ans += (R[r]-1) * (C[c]-1)

print(ans)