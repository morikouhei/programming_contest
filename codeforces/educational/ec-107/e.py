n,m = map(int,input().split())
S = [input() for i in range(n)]
mod = 998244353
ans = 0
count = 0
for i in range(n):
    for j in range(m):
        if S[i][j] == "o":
            count += 1

pow2 = [1]
for i in range(count+2):
    pow2.append(pow2[-1]*2%mod)
N = [0]
for i in range(max(n,m)+2):
    N.append((pow2[i]-N[-1])%mod)

for i in range(n):
    c = 0
    for j in range(m):
        if S[i][j] != "o":
            c = 0
            continue
        if j != m-1 and S[i][j+1] == "o":
            ans += pow2[count-c-2]*N[c+1]
            ans %= mod
            c += 1

for i in range(m):
    c = 0
    for j in range(n):
        if S[j][i] != "o":
            c = 0
            continue
        if j != n-1 and S[j+1][i] == "o":
            ans += pow2[count-c-2]*N[c+1]
            ans %= mod
            c += 1
print(ans)