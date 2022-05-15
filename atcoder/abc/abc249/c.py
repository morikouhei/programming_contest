n,k = map(int,input().split())
S = [input() for i in range(n)]
ans = 0
for i in range(1<<n):
    count = [0]*26
    for j in range(n):
        if i >> j & 1:
            for s in S[j]:
                count[ord(s)-ord("a")] += 1
    num = 0
    for j in range(26):
        if count[j] == k:
            num += 1
    ans = max(ans,num)
print(ans)