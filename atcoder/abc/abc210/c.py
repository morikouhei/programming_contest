n,k = map(int,input().split())
C = list(map(int,input().split()))
ans = 0
dic = {}
s = set()
for i in range(n):
    dic[C[i]] = dic.get(C[i],0)+1
    s.add(C[i])

    if i >= k-1:
        ans = max(ans,len(s))
        dic[C[i-k+1]] -= 1
        if dic[C[i-k+1]] == 0:
            s.remove(C[i-k+1])
print(ans)

