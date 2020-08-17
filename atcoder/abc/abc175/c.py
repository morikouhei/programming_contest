x,k,d = map(int,input().split())
if x < 0:
    x = -x
if x >= k*d:
    print(x-k*d)
    exit()
k -= x//d
x -= x//d*d

if k%2 == 0:
    print(x)
else:
    print(abs(x-d))

