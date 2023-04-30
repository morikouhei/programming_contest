import bisect

n,m,k = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(n)]
CD = [list(map(int,input().split())) for i in range(m)]

def calc(x):
    l = []
    for c,d in CD:
        l.append(x*(c+d)-100*c)
    l.sort()

    count = 0
    for a,b in AB:
        t = x*(a+b)-100*a
        count += bisect.bisect_left(l,-t)
    
    return count

l = 0
r = 100

for i in range(50):
    x = (r+l)/2
    if calc(x) >= k:
        l = x
    else:
        r = x
print(l)