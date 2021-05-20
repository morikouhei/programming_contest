n = int(input())
A = list(map(int,input().split()))
dic = {0:1}
now = 0
ans = 0
for i,a in enumerate(A):
    if i % 2:
        now -= a
    else:
        now += a
    ans += dic.get(now,0)
    dic[now] = dic.get(now,0)+1
print(ans)
    