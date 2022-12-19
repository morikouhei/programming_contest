n,m = map(int,input().split())
S = []
ok = (1<<m)-1
for i in range(n):
    s = input()
    count = 0
    for j in range(m):
        if s[j] == "o":
            count += 1<<j

    S.append(count)
ans = 0
for i in range(n):
    for j in range(i):
        if S[i]|S[j] == ok:
            ans += 1
print(ans)