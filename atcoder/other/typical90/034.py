n,k = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
now = 0
count = 0
dic = {}
for i,a in enumerate(A,1):
    dic[a] = dic.get(a,0) + 1
    if dic[a] == 1:
        count += 1
    while count > k:
        dic[A[now]] -= 1
        if dic[A[now]] == 0:
            count -= 1
        now += 1
    ans = max(ans,i-now)
print(ans)