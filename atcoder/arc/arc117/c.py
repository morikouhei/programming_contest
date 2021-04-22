n = int(input())
C = input()
dic = {"R":0, "W":1, "B":2}
mod = 3

cum = [1]
cum_mod = [0]
for i in range(1,n+1):
    count = 0
    now = i
    while now % mod == 0:
        now //= mod
        count += 1
    cum.append((cum[-1]*now)%mod)
    cum_mod.append(cum_mod[-1]+count)

def nCr(n,r,mod):
    if n < r or r < 0:
        return 0
    if cum_mod[n] > cum_mod[r]+cum_mod[n-r]:
        return 0

    return cum[n]*cum[r]*cum[n-r]%mod

ans = 0
for i in range(n):
    ans += nCr(n-1, i, mod)*dic[C[i]]
    ans %= mod
if n%2 == 0:
    ans *= -1

ans %= mod
if ans == 0:
    print("R")
elif ans == 1:
    print("W")
else:
    print("B")