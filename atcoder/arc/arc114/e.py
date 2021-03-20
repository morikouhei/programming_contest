H,W = map(int,input().split())
h1,w1,h2,w2 = map(int,input().split())

if h2 > h1:
    h1,h2 = h2,h1
if w2 > w1:
    w1,w2 = w2,w1
mod = 998244353

ans = 1
base = h1-h2+w1-w2
for i in range(h1+1,H):
    ans += pow(i-h1+base,mod-2,mod)
    ans %= mod
for i in range(w1+1,W):
    ans += pow(i-w1+base,mod-2,mod)
    ans %= mod
for i in range(1,h2):
    ans += pow(h2-i+base,mod-2,mod)
    ans %= mod
for i in range(1,w2):
    ans += pow(w2-i+base,mod-2,mod)
    ans %= mod
print(ans)