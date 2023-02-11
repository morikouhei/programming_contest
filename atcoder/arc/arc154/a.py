n = int(input())
A = list(map(int,input()))
B = list(map(int,input()))
mod = 998244353

nA = 0
nB = 0
large = 0
for a,b in zip(A,B):
    a,b = min(a,b),max(a,b)
    nA = (nA*10+a)%mod
    nB = (nB*10+b)%mod

print(nA*nB%mod)