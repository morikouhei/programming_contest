n,l,r = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)
bases = []

for a in A:
    for b in bases:
        a = min(a,a^b)
    
    if a:
        bases.append(a)


bases.sort()
for i in range(len(bases)):
    b = bases[i].bit_length()-1
    for j in range(i+1,len(bases)):
        if bases[j] >> b & 1:
            bases[j] ^= bases[i]
bases += [0]*60
l -= 1

for i in range(l,r):
    ans = 0
    for j in range(60):
        if i >> j & 1:
            ans ^= bases[j]
    print(ans)
