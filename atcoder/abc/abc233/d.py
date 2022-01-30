n,k = map(int,input().split())
A = list(map(int,input().split()))
dic = {}
dic[0] = 1
ans = 0
cum = 0
for a in A:
    cum += a
    ans += dic.get(cum-k,0)
    dic[cum] = dic.get(cum,0)+1
print(ans)