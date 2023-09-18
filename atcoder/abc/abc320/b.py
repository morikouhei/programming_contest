S = input()
ans = 1
n = len(S)
for i in range(n):
    for j in range(i+1,n+1):
        s = S[i:j]
        if s == s[::-1]:
            ans = max(ans,len(s))
print(ans)