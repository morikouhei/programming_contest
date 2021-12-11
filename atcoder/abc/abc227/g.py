n,k = map(int,input().split())
mod = 998244353
m = max(int(n**0.5),k)
prime = [0]*(m+1)
fact = []
for i in range(2,m+1):
    if prime[i]:
        continue
    fact.append(i)
    for j in range(i,m+1,i):
        prime[j] = 1


ans = 1
A = [i for i in range(k+1)]
B = [i for i in range(n-k+1,n+1)]

for f in fact:
    count = 0
    for i in range(f,k+1,f):
        while A[i]%f == 0:
            A[i] //= f
            count -= 1

    s = (n-k+f)//f*f
    ind = s-(n-k+1)
    for i in range(ind,k,f):
        while B[i]%f == 0:
            B[i] //= f
            count += 1
    ans *= count+1
    ans %= mod
for b in B:
    if b == 1:
        continue
    ans *= 2
    ans %= mod
print(ans)