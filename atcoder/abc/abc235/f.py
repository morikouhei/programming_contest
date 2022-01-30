n = input()
m = int(input())
C = list(map(int,input().split()))
mod = 998244353

lowdp = [0]*(1<<10)
lowcountdp = [0]*(1<<10)
samedp = [0]*(1<<10)
samecountdp = [0]*(1<<10)
s = int(n[0])
for i in range(1,s+1):
    if i < s:
        lowdp[1<<i] = i
        lowcountdp[1<<i] = 1

    if i == s:
        samedp[1<<s] = s
        samecountdp[1<<s] = 1

for s in n[1:]:
    s = int(s)

    nlowdp = [0]*(1<<10)
    nlowcountdp = [0]*(1<<10)
    nsamedp = [0]*(1<<10)
    nsamecountdp = [0]*(1<<10)

    for i in range(1<<10):
        if samedp[i] == 0:
            continue
        for j in range(10):
            if j > s:
                continue
            if j < s:
                nlowdp[i|1<<j] += samedp[i]*10+j*samecountdp[i]
                nlowdp[i|1<<j] %= mod
                nlowcountdp[i|1<<j] += samecountdp[i]
                nlowcountdp[i|1<<j] %= mod
                # print(1,i,j,i|1<<j,nlowdp[i|1<<j])
            if j == s:
                nsamedp[i|1<<j] += samedp[i]*10+j*samecountdp[i]
                nsamedp[i|1<<j] %= mod
                nsamecountdp[i|1<<j] += samecountdp[i]
                nsamecountdp[i|1<<j] %= mod
                # print(2,i,j,i|1<<j,nsamedp[i|1<<j])

    for i in range(1<<10):
        if lowdp[i] == 0:
            continue
        for j in range(10):
            nlowdp[i|1<<j] += lowdp[i]*10+j*lowcountdp[i]
            nlowdp[i|1<<j] %= mod
            nlowcountdp[i|1<<j] += lowcountdp[i]
            nlowcountdp[i|1<<j] %= mod
            # print(3,i,j,i|1<<j,nlowdp[i|1<<j])

    for i in range(1,10):
        nlowdp[1<<i] += i
        nlowcountdp[1<<i] += 1

    lowdp = nlowdp
    samedp = nsamedp
    lowcountdp = nlowcountdp
    samecountdp = nsamecountdp


b = 0
for c in C:
    b |= 1<<c
ans = 0

for i in range(1<<10):
    if i|b == i:
        ans += lowdp[i]
        ans += samedp[i]
        ans %= mod
print(ans)
