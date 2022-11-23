n,m = map(int,input().split())
P = list(map(int,input().split()))

mod = 998244353
ans = 0
used = [0]*n
num = n

cand = 1
for i,p in enumerate(P):
    p -= 1
    print(i,p,ans)
    if used[i] and used[p]:
        continue
    if i == p:
        cand *= m
        cand %= mod

    elif used[i] + used[p] == 0:

        ans += m*(m-1)//2*cand%mod*pow(m,num-2,mod)%mod
        ans %= mod
        cand *= m
        cand %= mod
        num -= 2
    else:
        ans += (m-1)*cand//2%mod*pow(m,num-1,mod)%mod
        ans %= mod
        num -= 1
    used[i] = used[p] = 1
    print(i,p,ans)
print(ans)