mod = 998244353

def solve():
    n = int(input())
    S = input()
    ans = 0
    for i in range((n+1)//2):
        num = ord(S[i])-ord("A")
        ans += num*pow(26,(n+1)//2-i-1,mod)%mod
        ans %= mod
    half = S[:n//2][::-1]

    if S[:(n+1)//2]+half <= S:

        ans += 1
    print(ans%mod)
    return 
t = int(input())
for _ in range(t):
    solve()