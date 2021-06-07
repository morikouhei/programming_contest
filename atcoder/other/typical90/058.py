n,k = map(int,input().split())
mod = 10**5

l = [n]
x = n
while True:
    y = sum([int(i) for i in str(x)])
    x = (x+y)%mod
    if x in l:
        break
    l.append(x)

ind = l.index(x)
if len(l) > k:
    print(l[k])
else:
    k -= ind
    le = len(l)-ind
    print(l[ind+k%le])
