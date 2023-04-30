import bisect
n,m,k = map(int,input().split())
S = input()
pos = []
for i,s in enumerate(S):
    if s == "x":
        pos.append(i)


ans = 0
if k == len(pos)*m:
    print(n*m)
    exit()

size = len(pos)
now = 0

for i,s in enumerate(S):
    if k < size-now:
        target = pos[now+k]
        ans = max(ans,target-i)
        # print(i,target,target-i,k,size,now,size-now-k)
        if s == "x":
            now += 1
        continue

    lk = k - (size-now)

    mul,dk = divmod(lk,size)

    if mul == m-1:
        le = n-i + mul * n
    else:
        le = n-i + mul * n + pos[dk]
    # print(mul,le,ans)
    ans = max(ans,le)

    if s == "x":
        now += 1

print(ans)

# ooxoo
# ooxoo
# ooxoo
# ooxooooxooooxooooxoo